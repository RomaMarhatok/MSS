from ..models import Patient
from ..serializers.user_serializer import UserSerializer
from ..serializers.user_personal_info_serializer import UserPersonalInfoSerializer
from rest_framework import status
from django.http import HttpRequest
from ..utils.list_utils import is_containe
from ..services.model_services.user_service import UserService


class RegistrationService:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.user_service = UserService()

    def register_user(self):
        validated_request_data, request_data_is_valid = self.__validate_request_data()
        if request_data_is_valid:
            return self.__processing_registration(validated_request_data)
        return validated_request_data

    def __validate_request_data(self):
        validating_keys = ["login", "password", "first_name", "second_name"]
        request_keys = list(self.request.data.keys())
        if is_containe(validating_keys, request_keys):
            return (
                {
                    "user": {
                        "login": self.request.data["login"],
                        "password": self.request.data["password"],
                    },
                    "first_name": self.request.data["first_name"],
                    "second_name": self.request.data["second_name"],
                },
                True,
            )
        return (
            {
                "data": {
                    "errors": ["login,password,first_name,second_name don't provided"]
                },
                "status": status.HTTP_400_BAD_REQUEST,
            },
            False,
        )

    def __processing_registration(self, data: dict):
        if not self.user_service.is_user_exist(
            data["user"]["login"], data["user"]["password"]
        ):
            serialization_result = self.__init__user(data)
            return serialization_result
        return {
            "data": {"errors": {"general": ["user already exist"]}},
            "status": status.HTTP_400_BAD_REQUEST,
        }

    def __init__user(self, data):
        user_serializer = UserSerializer(data=data["user"])
        if user_serializer.is_valid():
            user = user_serializer.save()
            Patient.objects.create(user=user)

            personl_info_serializer = UserPersonalInfoSerializer(data=data)
            if personl_info_serializer.is_valid():
                personl_info_serializer.save()
                return {
                    "data": {"message": "user was successful registrated"},
                    "status": status.HTTP_200_OK,
                }
            return {
                "data": {"errors": personl_info_serializer.errors},
                "status": status.HTTP_400_BAD_REQUEST,
            }

        return {
            "data": {"errors": user_serializer.errors},
            "status": status.HTTP_400_BAD_REQUEST,
        }
