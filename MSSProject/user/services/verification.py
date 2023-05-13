from django.http import HttpResponse
from django.db import transaction
from django.utils.http import urlsafe_base64_decode
from user.repositories import UserRepository


class VerificationService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    @transaction.atomic
    def verify(self, uid, token):
        # декодирование логина
        login = urlsafe_base64_decode(uid).decode()
        # верификация пользователя
        self.user_repository.verify_user(login, token)
        return HttpResponse()
