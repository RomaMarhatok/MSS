from rest_framework.serializers import ModelSerializer
from ..models import DoctorSpecialization


class DoctorSpecializationSerializer(ModelSerializer):
    class Meta:
        model = DoctorSpecialization
        fields = (
            "name",
            "slug",
        )
        extra_kwargs = {
            "url": {"lookup_field": "slug"},
            "slug": {"required": False, "validators": []},
            "name": {"required": False, "validators": []},
        }
