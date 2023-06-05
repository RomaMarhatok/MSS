# stdlib imports
import os
from dataclasses import dataclass
# core django imports
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.db import transaction
from django.contrib.auth.hashers import make_password
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
        # формирование данных
        login = data.get("login", None)
        password = data.get("password", None)
        salt = os.environ.get("HASHER_SALT", None)
        hashed_password = make_password(password, salt)
        # проверка существования пользователя
        if (
            login is not None or password is not None
        ) and self.user_repository.is_exist(login=login, password=hashed_password):
            # получение данных пользователя
            user = self.user_repository.get(login=login)
            # если пользователь не верифицирован то вызвать исключение
            if not user.verified:
                raise exceptions.AuthenticationFailed(
                    detail={
                        "message": "Пользователь не верефицирован",
                        "description": "Пользователь не верефицирован",
                    }
                )
            # создать токен аутентификации
            token, _ = Token.objects.get_or_create(user=user)
            # отправка запроса
            return JsonResponse(
                data={
                    "message": "Пользователь авторизирован",
                    "token": token.key,
                    "role": user.role.name,
                    "slug": user.slug,
                },
            )
        # если пользователь не найден то вызвать исключение
        raise exceptions.NotFound(
            detail={
                "message": "Не валидные данные в запросе",
                "description": "Пользователь с такими данными не существует",
            }
        )
