# stdlib imports
from typing import OrderedDict

# Third-party app imports
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    CharField,
)

# app imports
from ..models import Role, User
from common.validators.login_validator import LoginValidator
from common.validators.password_validator import PasswordValidator

# override login field - for put away default validators
# role and slug is default field and because i set them how SerializerMethodField


class UserSerializer(ModelSerializer):
    login = CharField()
    role = SerializerMethodField()
    slug = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "login",
            "password",
            "verified",
            "slug",
            "role",
        )

    def get_slug(self, instance: User):
        return instance.slug

    def get_role(self, instance: User):
        return instance.role

    def validate_password(self, value):
        if not PasswordValidator.is_valid(value):
            message = (
                "Введите валидный пароль. Пароль может содержать только Английские символы и числа"
                "минимальная длинна пароля 8"
            )
            raise ValidationError(message)
        return value

    def validate_login(self, value):
        if User.objects.filter(login=value).exists():
            message = "Пользователь с таким логином уже существует"
            raise ValidationError(message)
        if not LoginValidator.is_valid(value):
            message = (
                "Введите валидный логин. Логин может содержать только Английские символы, "
                "числа, и эти сиволы '_', '-'."
            )
            raise ValidationError(message)
        return value

    def create(self, validated_data: OrderedDict) -> User:
        if "role" in validated_data:
            validated_data.pop("role")
        role = Role.objects.get(name=Role.PATIENT)
        instance = User.objects.create(**validated_data, role=role)
        return instance

    def to_representation(self, instance: User):
        rep = super().to_representation(instance)
        rep.pop("login")
        rep.pop("password")
        rep["role"] = instance.role.name
        if hasattr(instance, "userpersonalinfo"):
            rep["full_name"] = instance.userpersonalinfo.full_name
        return rep
