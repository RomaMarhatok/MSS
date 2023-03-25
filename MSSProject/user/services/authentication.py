from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpRequest
from user.repositories import UserRepository
from dataclasses import dataclass


@dataclass
class AuthenticationService:
    user_repository = UserRepository()

    def authenticate(self, request: HttpRequest):
        if self._is_valid(request):
            return self._get_response(request.data["login"], request.data["password"])
        return {
            "data": {"errors": {"general": ["login or password don't provided"]}},
            "status": status.HTTP_400_BAD_REQUEST,
        }

    def _is_valid(self, request: HttpRequest) -> bool:
        return "login" in request.data and "password" in request.data

    def _get_response(self, login, password):
        if self.user_repository.is_exist(login=login, password=password):
            user = self.user_repository.get(login=login)
            token, _ = Token.objects.get_or_create(user=user)
            return {
                "data": {
                    "message": "user successful authenticated",
                    "token": token.key,
                    "role": user.role.name,
                    "slug": user.slug,
                },
                "status": status.HTTP_200_OK,
            }

        return {
            "data": {"errors": {"general": ["user don't exist"]}},
            "status": status.HTTP_403_FORBIDDEN,
        }
