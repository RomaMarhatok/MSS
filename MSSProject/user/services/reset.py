from django.http import HttpResponse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from user.repositories import UserPersonalInfoRepository
from user.repositories import UserRepository
from django.utils.http import urlsafe_base64_decode


class ResetPasswordService:
    def __init__(self) -> None:
        self.user_personal_info = UserPersonalInfoRepository()
        self.user_repository = UserRepository()
        self.reset_password_token_generator = PasswordResetTokenGenerator()

    def reset_password(self, data: dict):
        token = data.get("token", None)
        password = data.get("password", None)
        uid = data.get("uid", None)
        login = urlsafe_base64_decode(uid).decode()
        user = self.user_repository.get(login=login)
        if self.reset_password_token_generator.check_token(user, token):
            self.user_repository.change_password(user, password)
            return HttpResponse()
