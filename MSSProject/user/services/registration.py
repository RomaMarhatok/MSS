from django.http import HttpResponse, JsonResponse
from django.db import transaction

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

    @transaction.atomic
    def registrate(self, data: dict) -> HttpResponse:
        user = self.user_repository.create(data)

        data.update({"user_slug": user.slug})

        self.user_personal_info_repository.create(data)

        self.user_location_repository.create(data)

        return JsonResponse(data={"message": "user was successful registrated"})
