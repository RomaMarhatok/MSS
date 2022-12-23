from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .role_serializer import RoleSerializer
from ..models import (
    User,
    Role,
)
from rest_framework.serializers import ValidationError
from ..validators.password_validator import PasswordValidator
from ..validators.login_validator import LoginValidator
from ..validators.text_validator import TextValidator


class UserSerializer(ModelSerializer):
    role = RoleSerializer(many=False, required=False)

    class Meta:
        model = User
        fields = (
            "login",
            "password",
            "slug",
            "role",
        )
        extra_kwargs = {
            "login": {
                "validators": [],
            },
            "slug": {"required": False},
        }
        lookup_field = "slug"

    def validate_password(self, value):
        if not PasswordValidator.is_valid(value):
            message = (
                "Enter a valid password. This value may contain only English letters and numbers "
                "min length of password 8 max length pasword 15"
            )
            raise ValidationError(message)
        return value

    def validate_login(self, value):
        if not LoginValidator.is_valid(value):
            message = (
                "Enter a valid login. This value may contain only English letters, "
                "numbers, and optinal contain '_', '-' characters."
            )
            raise ValidationError(message)
        return value

    def create(self, validated_data: OrderedDict) -> User:
        role, validated_data = self.__get_role(validated_data)
        instance, _ = User.objects.get_or_create(**validated_data, role=role)
        return instance

    def __get_role(self, validated_data: OrderedDict) -> Role:
        role = None
        if "role" in validated_data:
            role = Role.objects.get(name=validated_data["role"]["name"])
            validated_data.pop("role")
        else:
            role = Role.objects.get(name="patient")
        return role, validated_data
