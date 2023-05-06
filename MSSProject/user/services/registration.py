from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
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

    @transaction.atomic
    def registrate(self, data: dict) -> HttpResponse:
        user = self.user_repository.create(data)

        data.update({"user_slug": user.slug})

        user_personal_info = self.user_personal_info_repository.create(data)

        self.user_location_repository.create(data)
        if "email_message" in data:
            self.email_service.send_verification_email(
                user_personal_info.email, data["email_message"]
            )
        return JsonResponse(
            data={
                "message": "Пользователь зарегистрирован",
                "token": urlsafe_base64_encode(force_bytes(user.login)),
                "email": user_personal_info.email,
            }
        )
