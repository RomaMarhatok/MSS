from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import (
    User,
    UserPersonalInfo,
)
from rest_framework.serializers import ValidationError
from ..validators.text_validator import TextValidator
from .user_serializer import UserSerializer


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

    def to_representation(self, instance: UserPersonalInfo):
        rep = super().to_representation(instance)
        rep.pop("user")
        if (
            "not_necessary_fields" in self.context
            and self.context["not_necessary_fields"] is not None
        ):
            for field in self.context["not_necessary_fields"]:
                if field in rep:
                    rep.pop(field)
        full_name = self.__get_full_name(rep)
        rep.update({"full_name": full_name})
        if not instance.image.storage.exists(instance.image.name):
            rep.pop("image")
        return rep

    def __get_full_name(self, personal_info: dict):
        return (
            personal_info.get("first_name", "")
            + " "
            + personal_info.get("second_name", "")
            + " "
            + personal_info.get("patronymic", "")
        )
