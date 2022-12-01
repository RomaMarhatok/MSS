from rest_framework.serializers import ModelSerializer
from ..models import ImageForAnalyzes


class ImageForAnlyzeSerializer(ModelSerializer):
    class Meta:
        model = ImageForAnalyzes
        fields = (
            "image",
            "description",
        )
