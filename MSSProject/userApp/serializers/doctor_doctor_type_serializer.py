from rest_framework.serializers import ModelSerializer
from ..models import DoctorDoctorSpecialization


class DoctorDoctorSpecializationSerializer(ModelSerializer):
    class Meta:
        model = DoctorDoctorSpecialization
        fields = (
            "doctor",
            "doctor_specialization",
        )
