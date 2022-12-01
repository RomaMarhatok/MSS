from rest_framework.serializers import ModelSerializer
from ..models import DoctorType


class DoctorTypeSerializer(ModelSerializer):
    class Meta:
        model = DoctorType
        fields = (
            "doctor_type",
            "slug",
        )
        extra_kwargs = {
            "doctor_type": {"validators": []},
            "url": {"lookup_field": "slug"},
            "slug": {"required": False},
        }
