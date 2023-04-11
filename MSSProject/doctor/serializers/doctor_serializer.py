from typing import OrderedDict
from rest_framework.serializers import ModelSerializer, SlugField
from ..models import Doctor
from user.models import User


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
