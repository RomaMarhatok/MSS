from django.http import HttpResponse
from django.db import transaction
from django.utils.http import urlsafe_base64_decode
from user.repositories import UserRepository


class VerificationService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    @transaction.atomic
    def verify(self, token):
        login = urlsafe_base64_decode(token).decode()
        print(login)
        self.user_repository.verify_user(login)
        return HttpResponse()
