from ..models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpRequest
from ..utils.list_utils import is_containe


class AuthenticationService:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    def authenticate_user(self):
        request_data, request_data_is_valid = self.__validate_request_data()
        if request_data_is_valid:
            return self.__processing_authentication(
                request_data["login"], request_data["password"]
            )
        return request_data

    def __validate_request_data(self):
        validating_keys = ["login", "password"]
        request_keys = self.request.data.keys()
        if is_containe(validating_keys, request_keys):
            return (
                {
                    "login": self.request.data["login"],
                    "password": self.request.data["password"],
                },
                True,
            )
        return (
            {
                "data": {"errors": ["login or password don't provided"]},
                "status": status.HTTP_400_BAD_REQUEST,
            },
            False,
        )

    def __processing_authentication(self, login, password):
        if User.is_exist(login, password):
            user = User.get_user_by_login(login)
            token, _ = Token.objects.get_or_create(user=user)
            return {
                "data": {
                    "message": "user successful authenticated",
                    "token": token.key,
                    "user_role": user.role.name,
                    "user_slug": user.slug,
                },
                "status": status.HTTP_200_OK,
            }

        return {
            "data": {"errors": ["user don't exist"]},
            "status": status.HTTP_403_FORBIDDEN,
        }