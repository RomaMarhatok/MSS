from rest_framework.serializers import ModelSerializer
from ..models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "name",
            "slug",
        )
        extra_kwargs = {
            "name": {
                "validators": [],
            },
            "slug": {"required": False},
            "url": {"lookup_field": "slug"},
        }
