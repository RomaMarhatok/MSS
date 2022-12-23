from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .role_serializer import RoleSerializer
from ..models import (
    User,
    Role,
    UserPersonalInfo,
    Document,
    DocumentType,
    UserLocation,
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


class UserPersonalInfoSerializer(ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = UserPersonalInfo
        fields = (
            "user",
            "image",
            "first_name",
            "second_name",
            "patronymic",
            "email",
            "gender",
            "age",
            "health_status",
        )
        extra_kwargs = {
            "image": {"required": False},
            "patronymic": {"required": False},
            "email": {"required": False},
            "gender": {"required": False},
            "age": {"required": False},
            "health_status": {"required": False},
        }

    def validate_first_name(self, value):
        if not TextValidator.is_valid(value):
            message = "this field may contain only English letter"
            raise ValidationError(message)
        return value

    def validate_second_name(self, value):
        if not TextValidator.is_valid(value):
            message = "this field may contain only English letter"
            raise ValidationError(message)
        return value

    def create(self, validated_data: OrderedDict) -> UserPersonalInfo:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        instance, _ = UserPersonalInfo.objects.get_or_create(
            **validated_data, user=user
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("user")
        return rep


class UserDocumentTypeSerializer(ModelSerializer):
    class Meta:
        fields = (
            "name",
            "slug",
        )
        model = Document
        extra_kwargs = {
            "slug": {"required": False},
        }


class UserDocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)
    document_type = UserDocumentTypeSerializer(many=False, required=True)

    class Meta:
        model = Document
        fields = (
            "name",
            "slug",
            "user",
            "content",
            "document_type",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "user": {"validators": [], "lookup_field": "slug"},
            "document_type": {"validators": []},
            "name": {"validators": []},
            "slug": {"required": False},
            "created_at": {"required": False},
            "updated_at": {"required": False},
        }

    def create(self, validated_data: OrderedDict) -> Document:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        document_type = Document.objects.get(
            name=validated_data["document_type"]["name"]
        )
        validated_data.pop("document_type")
        instance, _ = Document.objects.get_or_create(
            **validated_data, user=user, document_type=document_type
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("user")
        if "include_context" in self.context and self.context["include_context"]:
            rep.pop("content")
        return rep


class UserLocationSerializer(ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserLocation
        fields = (
            "user",
            "country",
            "city",
            "address",
        )

    def create(self, validated_data):
        user_login = validated_data["user"]["login"]
        user = User.objects.get(login=user_login)
        validated_data.pop("user")
        instance, _ = UserLocation.objects.get_or_create(**validated_data, user=user)
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("user")
        return rep
