from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import DoctorType, Doctor, User, DoctorDoctorTypes
from .user_serializer import UserSerializer


class DoctorTypeSerializer(ModelSerializer):
    class Meta:
        model = DoctorType
        fields = ("doctor_type",)
        extra_kwargs = {"doctor_type": {"validators": []}}


class DoctorSerializer(ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Doctor
        fields = ("user",)
        extra_kwargs = {"user": {"validators": []}}

    def create(self, validated_data: OrderedDict) -> Doctor:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        instance, _ = Doctor.objects.get_or_create(user=user)
        return instance

    def to_representation(self, instance: Doctor) -> dict[User, list[DoctorType]]:
        user_from_instance = instance.user
        doctor_types = [
            DoctorTypeSerializer(instance=doctor_doctor_type.doctor_type).data
            for doctor_doctor_type in DoctorDoctorTypes.objects.filter(
                doctor__pk=user_from_instance.pk
            )
        ]
        user = UserSerializer(instance=user_from_instance).data
        return {"user": user, "doctor_types": doctor_types}
