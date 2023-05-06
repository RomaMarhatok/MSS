# stdlib imports
from dataclasses import dataclass

# core django imports
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.db import transaction

# Third-party app import
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

# imports from apps
from user.repositories import UserRepository


@dataclass
class AuthenticationService:
    user_repository = UserRepository()

    @transaction.atomic
    def authenticate(self, data: dict) -> HttpResponse:
        login = data.get("login", None)
        password = data.get("password", None)
        if (
            login is not None or password is not None
        ) and self.user_repository.is_exist(login=login, password=password):
            user = self.user_repository.get(login=login)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse(
                data={
                    "message": "Пользователь авторизирован",
                    "token": token.key,
                    "role": user.role.name,
                    "slug": user.slug,
                },
            )
        raise exceptions.NotFound(
            detail={
                "message": "Не валидные данные в запросе",
                "description": "Пользователь с такими данными не существует",
            }
        )
