from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import (
    DoctorSpecialization,
    Doctor,
    User,
    DoctorDoctorSpecialization,
    UserPersonalInfo,
)
from .user_serializer import UserSerializer
from .doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from .user_personal_info_serializer import UserPersonalInfoSerializer


class DoctorSerializer(ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Doctor
        fields = ("user",)
        extra_kwargs = {
            "user": {"validators": []},
            "url": {"lookup_field": "user"},
        }

    def create(self, validated_data: OrderedDict) -> Doctor:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        instance, _ = Doctor.objects.get_or_create(user=user)
        return instance

    def to_representation(self, instance):
        return super().to_representation(instance)
