from rest_framework.serializers import HyperlinkedModelSerializer
from ..models import Role


class RoleSerializer(HyperlinkedModelSerializer):
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
