from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .role_serializer import RoleSerializer
from ..models import User, Role, UserPersonalInfo, UserDocument


class UserSerializer(ModelSerializer):
    role = RoleSerializer(many=False)

    class Meta:
        model = User
        fields = (
            "login",
            "password",
            "role",
        )
        extra_kwargs = {
            "login": {
                "validators": [],
            }
        }

    def create(self, validated_data: OrderedDict):
        role = Role.objects.get(name=validated_data["role"]["name"])
        validated_data.pop("role")
        return User.objects.get_or_create(**validated_data, role=role)


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

    def create(self, validated_data: OrderedDict):
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        return UserPersonalInfo.objects.get_or_create(**validated_data, user=user)


class UserDocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserDocument
        fields = (
            "user",
            "content",
        )
        extra_kwargs = {"user": {"validators": []}}

    def create(self, validated_data: OrderedDict):
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        return UserDocument.objects.create(**validated_data, user=user)
