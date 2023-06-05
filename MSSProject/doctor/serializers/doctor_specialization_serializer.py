from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import DoctorSpecialization


class DoctorSpecializationSerializer(ModelSerializer):
    slug = SerializerMethodField()

    class Meta:
        model = DoctorSpecialization
        fields = (
            "name",
            "slug",
        )

    def get_slug(self, instance: DoctorSpecialization):
        return instance.slug
