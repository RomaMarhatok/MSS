from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import ImageForAnalyzes


class ImageForAnlyzeSerializer(ModelSerializer):
    class Meta:
        model = ImageForAnalyzes
        fields = (
            "image",
            "description",
        )

    def create(self, validated_data: OrderedDict):
        return ImageForAnalyzes.objects.create(
            description=validated_data["description"], image=validated_data["image"]
        )
