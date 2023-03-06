from rest_framework.serializers import ModelSerializer
from ..models import (
    User,
    UserLocation,
)
from .user_serializer import UserSerializer


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
        location = rep.get("country", None) + " " + rep.get("city", None)
        rep.update({"location": location})
        return rep
