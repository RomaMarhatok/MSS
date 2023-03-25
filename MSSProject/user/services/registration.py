from django.http import HttpRequest
from user.services import UserService
from rest_framework import status


class RegistrationService:
    def registrate(self, request: HttpRequest):
        user_service = UserService()
        print(request.data)
        login = request.data.get("login", None)
        if login is None:
            return {
                "data": {"errors": {"general": ["login don't provided"]}},
                "status": status.HTTP_400_BAD_REQUEST,
            }
        if user_service.user_repository.is_exist(login=login):
            return {
                "data": {"errors": {"general": ["user already exist"]}},
                "status": status.HTTP_400_BAD_REQUEST,
            }
        return user_service.create_user(request.data)

    # for rollback
    # def register_user(self, request: HttpRequest):
    #     validated_request_data, request_data_is_valid = self._get_response(request)
    #     if request_data_is_valid:
    #         return self.__processing_registration(validated_request_data)
    #     return validated_request_data

    # def _get_response(self, request: HttpRequest):
    #     validating_keys = ["login", "password", "first_name", "second_name"]
    #     request_keys = list(request.data.keys())
    #     if is_containe(validating_keys, request_keys):
    #         return (
    #             {
    #                 "user": {
    #                     "login": request.data["login"],
    #                     "password": request.data["password"],
    #                 },
    #                 "first_name": request.data["first_name"],
    #                 "second_name": request.data["second_name"],
    #             },
    #             True,
    #         )
    #     return (
    #         {
    #             "data": {
    #                 "errors": ["login,password,first_name,second_name don't provided"]
    #             },
    #             "status": status.HTTP_400_BAD_REQUEST,
    #         },
    #         False,
    #     )

    # def __processing_registration(self, data: dict):
    #     if not self.user_service.user_repository.is_exist(
    #         login=data["user"]["login"], password=data["user"]["password"]
    #     ):
    #         serialization_result = self.__init__user(data)
    #         return serialization_result
    #     return {
    #         "data": {"errors": {"general": ["user already exist"]}},
    #         "status": status.HTTP_400_BAD_REQUEST,
    #     }

    # def __init__user(self, data: dict):
    #     user_serializer = UserSerializer(data=data["user"])
    #     if user_serializer.is_valid():
    #         user = user_serializer.save()
    #         Patient.objects.create(user=user)

    #         personl_info_serializer = UserPersonalInfoSerializer(data=data)
    #         if personl_info_serializer.is_valid():
    #             personl_info_serializer.save()
    #             return {
    #                 "data": {"message": "user was successful registrated"},
    #                 "status": status.HTTP_200_OK,
    #             }
    #         return {
    #             "data": {"errors": personl_info_serializer.errors},
    #             "status": status.HTTP_400_BAD_REQUEST,
    #         }

    #     return {
    #         "data": {"errors": user_serializer.errors},
    #         "status": status.HTTP_400_BAD_REQUEST,
    #     }
