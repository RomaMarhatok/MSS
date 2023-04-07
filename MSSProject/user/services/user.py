from django.http import HttpRequest, HttpResponse, JsonResponse
from responses.errors import JsonResponseBadRequest

from ..models import User, UserLocation, UserPersonalInfo
from ..repositories import (
    UserLocationRepository,
    UserPersonalInfoRepository,
    UserRepository,
)
from ..serializers import (
    UserLocationSerializer,
    UserPersonalInfoSerializer,
)


class UserService:
    def __init__(self) -> None:
        self.user_repository: UserRepository = UserRepository()
        self.user_personal_info_repository: UserPersonalInfoRepository = (
            UserPersonalInfoRepository()
        )
        self.user_location_repository: UserLocationRepository = UserLocationRepository()

    def get_user_info(self, slug, request: HttpRequest) -> HttpResponse:
        try:
            user = self.user_repository.get(slug=slug)
        except User.DoesNotExist:
            return JsonResponseBadRequest(
                data={
                    "message": "Записи не существует",
                    "description": f"Пользователь с таким slug {slug} не существует",
                }
            )

        try:
            user_personal_info = UserPersonalInfoSerializer(
                instance=user.userpersonalinfo, context={"request": request}
            ).data
        except UserPersonalInfo.DoesNotExist:
            user_personal_info = {}

        try:
            user_location = UserLocationSerializer(
                instance=user.userlocation,
            ).data
        except UserLocation.DoesNotExist:
            user_location = {}
        return JsonResponse(data={**user_personal_info, **user_location})

    def validate_user(self, data: dict) -> JsonResponse:
        login = data.get("login", None)
        if self.user_repository.is_exist(login=login):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидные данные в запросе",
                    "description": "Пользватель с таким логином уже существует",
                },
                status=400,
            )
        return HttpResponse()

    def validate_personal_info(self, data: dict) -> JsonResponse:
        email = data.get("email", None)
        if self.user_personal_info_repository.is_exist(email=email):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидные данные в запросе",
                    "description": "Пользователь с такой почтой уже существует",
                },
                status=400,
            )
        return HttpResponse()
