from rest_framework.serializers import ModelSerializer
from ..models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ("name",)
        extra_kwargs = {
            "name": {
                "validators": [],
            }
        }
