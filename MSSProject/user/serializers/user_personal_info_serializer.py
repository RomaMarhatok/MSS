from typing import OrderedDict
from rest_framework.serializers import (
    ModelSerializer,
    SlugField,
)

from ..models import User, UserPersonalInfo


class UserPersonalInfoSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")

    class Meta:
        model = UserPersonalInfo
        fields = (
            "user_slug",
            "first_name",
            "second_name",
            "patronymic",
            "full_name",
            "email",
            "gender",
            "age",
            "health_status",
        )

    def create(self, validated_data: OrderedDict) -> UserPersonalInfo:
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        instance = UserPersonalInfo.objects.create(**validated_data, user=user)
        return instance

    def validate_email(self, value):
        if (
            UserPersonalInfo.objects.filter(email=value).exists()
            and self.instance is None
        ):
            message = "Пользователь с такой почтой уже существует"
            raise ValueError(message)
        return value

    def update(self, instance: UserPersonalInfo, validated_data: OrderedDict):
        validated_data["user"] = instance.user
        return UserPersonalInfo.objects.filter(user__slug=instance.user.slug).update(
            **validated_data
        )

    def to_representation(self, instance: UserPersonalInfo):
        rep = super().to_representation(instance)
        if (
            "not_necessary_fields" in self.context
            and self.context["not_necessary_fields"] is not None
        ):
            for field in self.context["not_necessary_fields"]:
                if field in rep:
                    rep.pop(field)
        return rep
