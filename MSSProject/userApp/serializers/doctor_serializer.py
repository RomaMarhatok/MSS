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

    def create(self, validated_data: OrderedDict):
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        return Doctor.objects.get_or_create(user=user)

    def to_representation(self, instance: Doctor):
        user_from_instance = instance.user
        doctor_types = [
            DoctorTypeSerializer(data=doctor_doctor_type.doctor_type).data
            for doctor_doctor_type in DoctorDoctorTypes.objects.filter(
                doctor__pk=user_from_instance.pk
            )
        ]
        user = UserSerializer(instance=user_from_instance).data
        return {"user": user, "doctor_types": doctor_types}
