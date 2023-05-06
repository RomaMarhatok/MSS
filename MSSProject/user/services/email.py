import os
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import get_connection, send_mail
from rest_framework import exceptions
from .enums import EmailHost
from django.http import HttpResponse


class EmailService:
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

    def get_yandex_connection(self):
        print(os.environ.get("YANDEX_MAIL"))
        yandex_username = os.environ.get("YANDEX_MAIL")
        yandex_password = os.environ.get("YANDEX_PASSWORD")
        return self._get_smtp_connection(
            EmailHost.YANDEX_HOST.value, yandex_username, yandex_password
        )

    def get_email_connection(self, email: str):
        if "yandex" in email:
            return self.get_yandex_connection()
        if "gmail" in email:
            return self.get_gmail_connection()
        raise exceptions.ValidationError(
            detail={
                "message": "Не валидные данные в запросе",
                "description": "Этот сервис не поддерживается (поддерживаются почты yandex,gmail)",
            }
        )

    def send_verification_email(self, data: dict) -> None:
        to_email = data.get("email", None)
        redirect_link = data.get("link", None)
        message = (
            f"Здравствуйте {to_email},\n"
            + "Если вы думаете что это не вы то проигнорируйте это сообщение"
            + f"Пожалуйста нажмите на ссылку для потверждения регистрации, {redirect_link}"
        )
        mail_subject = "Activate your account"
        conn = self.get_email_connection(to_email)
        from_email = (
            os.environ.get("YANDEX_MAIL")
            if not hasattr(conn, "username")
            else conn.username
        )
        send_mail(
            mail_subject,
            message,
            from_email,
            [to_email],
            connection=conn,
            fail_silently=False,
        )
        return HttpResponse()
