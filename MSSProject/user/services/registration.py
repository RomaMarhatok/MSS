from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import HttpResponse, JsonResponse
from django.db import transaction
from .email import EmailService
from user.repositories import (
    UserRepository,
    UserPersonalInfoRepository,
    UserLocationRepository,
)


class RegistrationService:
    def __init__(self) -> None:
        self.user_repository: UserRepository = UserRepository()
        self.user_personal_info_repository: UserPersonalInfoRepository = (
            UserPersonalInfoRepository()
        )
        self.user_location_repository: UserLocationRepository = UserLocationRepository()
        self.email_service = EmailService()
        self.verification_token_generation = PasswordResetTokenGenerator()

    @transaction.atomic
    def registrate(self, data: dict) -> HttpResponse:
        user = self.user_repository.create(data)

        data.update({"user_slug": user.slug})

        user_personal_info = self.user_personal_info_repository.create(data)

        self.user_location_repository.create(data)
        return JsonResponse(
            data={
                "message": "Пользователь зарегистрирован",
                "uid": urlsafe_base64_encode(force_bytes(user.login)),
                "token": self.verification_token_generation.make_token(user),
                "email": user_personal_info.email,
            }
        )
