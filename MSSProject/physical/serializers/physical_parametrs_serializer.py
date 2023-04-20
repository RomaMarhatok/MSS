from typing import OrderedDict
from rest_framework.serializers import ModelSerializer, SlugField
from ..models import PhysicalParameters
from user.models import User


class PhysicalParametersSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")

    class Meta:
        model = PhysicalParameters
        fields = (
            "user_slug",
            "weight",
            "height",
            "pressure",
        )

    def create(self, validated_data: OrderedDict):
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        return PhysicalParameters.objects.create(user=user, **validated_data)
