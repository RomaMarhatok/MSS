from django.db import transaction
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import exceptions
from ..models import UserLocation, UserPersonalInfo, Role
from ..repositories import (
    UserLocationRepository,
    UserPersonalInfoRepository,
    UserRepository,
)
from ..serializers import (
    UserSerializer,
    UserLocationSerializer,
    UserPersonalInfoSerializer,
)
from .mixins.is_user_exist_mixin import IsUserExistMixin
from physical.repositories import PhysicalParametersRepository
from physical.serializers import PhysicalParametersSerializer


class UserService(IsUserExistMixin):
    def __init__(self) -> None:
        self.user_repository: UserRepository = UserRepository()
        self.user_personal_info_repository: UserPersonalInfoRepository = (
            UserPersonalInfoRepository()
        )
        self.user_location_repository: UserLocationRepository = UserLocationRepository()
        self.physical_parameters_repository = PhysicalParametersRepository()

    def get_user_info(self, slug, request: HttpRequest) -> HttpResponse:
        if self.is_user_exist(slug):
            user = self.user_repository.get(slug=slug)
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

    @transaction.atomic
    def update_user_info(self, data: dict):
        user_slug = data.get("user_slug")
        self.is_user_exist(user_slug)
        user_personal_info = self.user_personal_info_repository.get(slug=user_slug)
        updated_user_personal_info = self.user_personal_info_repository.update(
            user_personal_info, data
        )
        user_personal_info_serializer = UserPersonalInfoSerializer(
            instance=updated_user_personal_info
        )
        physical_parameters_serailizer = self.physical_parameters_repository.list(
            patient_slug=user_slug
        )
        physical_parameters_serailizer = PhysicalParametersSerializer(
            instance=physical_parameters_serailizer, many=True
        )
        user_personal_info = user_personal_info_serializer.data
        user_personal_info.update(
            {
                "physical_parameters": physical_parameters_serailizer.data,
            }
        )
        return JsonResponse(data={"personal_info": user_personal_info})

    def get_all_patients(self):
        users = self.user_repository.list()
        serializerd_patients = []
        for user in users:
            if user.role is not None and user.role.name == Role.PATIENT:
                serializerd_patients.append(UserSerializer(instance=user).data)
        # serializerd_patients = [
        #     UserSerializer(instance=user).data
        #     for user in users
        #     if user.role.name == Role.PATIENT
        # ]
        return JsonResponse(
            data={
                "patients": serializerd_patients,
            }
        )

    def validate_user(self, data: dict) -> JsonResponse:
        login = data.get("login")
        if self.user_repository.is_exist(login=login):
            raise exceptions.ValidationError(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Пользватель с таким логином уже существует",
                },
            )
        return HttpResponse()

    def validate_personal_info(self, data: dict) -> JsonResponse:
        email = data.get("email")
        if self.user_personal_info_repository.is_exist(email=email):
            raise exceptions.ValidationError(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Пользователь с такой почтой уже существует",
                },
            )
        return HttpResponse()

    def get_cities(self):
        user_locations = self.user_location_repository.list()
        cities = list(user_locations.values_list("city", flat=True))
        return JsonResponse(
            data={
                "cities": cities,
            }
        )
