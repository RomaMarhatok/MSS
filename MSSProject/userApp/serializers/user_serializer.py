from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .role_serializer import RoleSerializer
from ..models import User, Role, UserPersonalInfo, UserDocument


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
        )

    def create(self, validated_data: OrderedDict) -> UserPersonalInfo:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        instance, _ = UserPersonalInfo.objects.get_or_create(
            **validated_data, user=user
        )
        return instance


class UserDocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserDocument
        fields = (
            "user",
            "content",
        )
        extra_kwargs = {"user": {"validators": []}}

    def create(self, validated_data: OrderedDict) -> UserDocument:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        instance, _ = UserDocument.objects.get_or_create(**validated_data, user=user)
        return instance
