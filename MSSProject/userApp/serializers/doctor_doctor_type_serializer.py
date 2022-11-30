from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .doctor_serializer import DoctorSerializer, DoctorTypeSerializer
from ..models import DoctorDoctorTypes


class DoctorDoctorTypesSerializer(ModelSerializer):
    doctor = DoctorSerializer(many=False, required=True)
    doctor_type = DoctorTypeSerializer(many=False, required=True)

    class Meta:
        model = DoctorDoctorTypes
        fields = ("doctor", "doctor_type")

    def create(self, validated_data: OrderedDict):
        pass
