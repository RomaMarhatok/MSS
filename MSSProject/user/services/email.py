import os
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import get_connection, send_mail
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import exceptions

from user.models import UserPersonalInfo
from user.repositories import UserRepository
from user.repositories import UserPersonalInfoRepository
from .enums import EmailHost


class EmailService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.user_personal_info_repository = UserPersonalInfoRepository()

    def _get_smtp_connection(
        self, host, username, password, use_tls=True, port=settings.EMAIL_PORT
    ) -> EmailBackend:
        conn = get_connection(
            host=host, port=port, username=username, password=password, use_tls=use_tls
        )
        return conn

    def get_gmail_connection(self):
        gmail_username = os.environ.get("GMAIL_MAIL")
        gmail_password = os.environ.get("GMAIL_PASSWORD")
        return self._get_smtp_connection(
            EmailHost.GMAIL_HOST.value, gmail_username, gmail_password
        )

    def get_yandex_connection(self) -> EmailBackend | None:
        yandex_username = os.environ.get("YANDEX_MAIL")
        yandex_password = os.environ.get("YANDEX_PASSWORD")
        return self._get_smtp_connection(
            EmailHost.YANDEX_HOST.value, yandex_username, yandex_password
        )

    def get_email_connection(self, email: str, fail_silently=False):
        if "yandex" in email:
            return self.get_yandex_connection()
        if "gmail" in email:
            return self.get_gmail_connection()
        if not fail_silently:
            raise exceptions.ValidationError(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Этот сервис не поддерживается (поддерживаются почты yandex,gmail)",
                }
            )
        else:
            return None

    def _get_message(self, to_email, redirect_link, is_reset_password=False):
        base_message = (
            f"Здравствуйте {to_email},\n"
            + "Если вы думаете что это не вы то проигнорируйте это сообщение\n"
        )
        if is_reset_password:
            return (
                base_message
                + f"Пожалуйста нажмите на ссылку для смены пароля, {redirect_link}"
            )

        return (
            base_message
            + f"Пожалуйста нажмите на ссылку для потверждения регистрации, {redirect_link}"
        )

    def _get_from_email(self, conn: EmailBackend):
        return (
            os.environ.get("YANDEX_MAIL")
            if not hasattr(conn, "username")
            else conn.username
        )

    def _get_mail_subject(self, is_reset_password=False):
        return "Потдверждение аккаунта" if not is_reset_password else "Изменение пароля"

    def _get_reset_password_link(self, email, link) -> str:
        try:
            user = self.user_personal_info_repository.get(email=email).user
            uid = urlsafe_base64_encode(force_bytes(user.login))
            token = PasswordResetTokenGenerator().make_token(user)
            link += f"{uid}/{token}/"
            return link
        except UserPersonalInfo.DoesNotExist:
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Пользователья с такой почтой не существует",
                }
            )

    def _send(
        self,
        mail_subject: str,
        message: str,
        from_email: str,
        to_email: list[str],
        connection: EmailBackend,
        fail_silently=False,
    ) -> None:
        send_mail(
            mail_subject,
            message,
            from_email,
            to_email,
            connection=connection,
            fail_silently=fail_silently,
        )

    def send(self, data: dict) -> None:
        redirect_link = data.get("link", None)
        is_reset_password = data.get("is_reset_password", False)
        to_email = data.get("email", None)
        if is_reset_password:
            redirect_link = self._get_reset_password_link(to_email, redirect_link)

        conn = self.get_email_connection(to_email)
        mail_subject = self._get_mail_subject(is_reset_password=is_reset_password)
        message = self._get_message(to_email, redirect_link, is_reset_password)
        from_email = self._get_from_email(conn)
        self._send(mail_subject, message, from_email, [to_email], conn)
        return HttpResponse()
