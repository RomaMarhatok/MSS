from rest_framework.serializers import (
    ChoiceField,
    ModelSerializer,
    SerializerMethodField,
)

from ..models import Role


class RoleSerializer(ModelSerializer):
    name = ChoiceField(
        choices=(("DOCTOR", "Doctor"), ("PATIENT", "Patient")),
        label="Role name",
        validators=[],
    )
    slug = SerializerMethodField()

    class Meta:
        model = Role
        fields = (
            "name",
            "slug",
        )

    def get_slug(self, instance: Role):
        return instance.slug
