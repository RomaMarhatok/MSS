from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import serializers
from common.repository.base_repository import AbstractRepository
from user.serializers import UserSerializer

from ..models import User


class UserRepository(AbstractRepository):
    class LoginSerializer(serializers.Serializer):
        login = serializers.CharField()

    class SlugSerializer(serializers.Serializer):
        slug = serializers.SlugField()

    def _validate_kwargs(self, kwargs) -> dict:
        login_serializer = self.LoginSerializer(data=kwargs)
        slug_serializer = self.SlugSerializer(data=kwargs)
        if login_serializer.is_valid():
            return login_serializer.validated_data
        elif slug_serializer.is_valid():
            return slug_serializer.validated_data
        raise ValueError(
            f"class:{self.__class__}\n"
            "function:[_validate_kwargs method]\n"
            "exception: Any kwargs arguments expected\n"
        )

    def is_exist(self, **kwargs) -> bool:
        data = self._validate_kwargs(kwargs)
        return User.objects.filter(**data).exists()

    def get(self, **kwargs) -> User:
        qs = User.objects.select_related("role", "userpersonalinfo", "userlocation")
        data = self._validate_kwargs(kwargs)
        return qs.get(**data)

    def list(self, **kwargs):
        qs = User.objects.select_related("role", "userpersonalinfo", "userlocation")
        return qs.all()

    def create(self, data: dict) -> User:
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_valid(self, data: dict) -> bool:
        serializer = UserSerializer(data=data)
        return serializer.is_valid(raise_exception=True)

    def verify_user(self, login: str, token: str) -> None:
        user = self.get(login=login)
        if PasswordResetTokenGenerator().check_token(user, token):
            user.verified = True
            user.save()
