from rest_framework.serializers import ModelSerializer, SlugField
from typing import OrderedDict
from ..models import Doctor

# user app import
from user.models import User
from user.serializers import UserSerializer


class DoctorSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")

    class Meta:
        model = Doctor
        fields = ("user_slug",)

    def create(self, validated_data: OrderedDict) -> Doctor:
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        instance, _ = Doctor.objects.get_or_create(user=user)
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
