from rest_framework.serializers import ModelSerializer
from ..models import DoctorSpecialization


class DoctorSpecializationSerializer(ModelSerializer):
    class Meta:
        model = DoctorSpecialization
        fields = (
            "doctor_type",
            "slug",
        )
        extra_kwargs = {
            "doctor_type": {"validators": []},
            "url": {"lookup_field": "slug"},
            "slug": {"required": False},
        }
