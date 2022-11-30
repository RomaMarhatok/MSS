from rest_framework.serializers import ModelSerializer
from ..models import DoctorDoctorTypes


class DoctorDoctorTypesSerializer(ModelSerializer):
    class Meta:
        model = DoctorDoctorTypes
        fields = (
            "doctor",
            "doctor_type",
        )
