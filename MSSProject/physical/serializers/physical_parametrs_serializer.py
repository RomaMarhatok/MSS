from typing import OrderedDict
from rest_framework.serializers import ModelSerializer, SlugField, SerializerMethodField
from ..models import PhysicalParameters
from user.models import User


class PhysicalParametersSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")
    slug = SerializerMethodField()
    created_at = SerializerMethodField()

    class Meta:
        model = PhysicalParameters
        fields = (
            "user_slug",
            "slug",
            "weight",
            "height",
            "pressure",
            "created_at",
        )

    def get_slug(self, instance: PhysicalParameters):
        return instance.slug

    def get_created_at(self, instance: PhysicalParameters):
        return instance.created_at

    def create(self, validated_data: OrderedDict):
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        return PhysicalParameters.objects.create(user=user, **validated_data)

    def update(self, instance: PhysicalParameters, validated_data: OrderedDict):
        if "user" in validated_data:
            validated_data.pop("user")
        return PhysicalParameters.objects.filter(user=instance.user).update(
            **validated_data
        )
