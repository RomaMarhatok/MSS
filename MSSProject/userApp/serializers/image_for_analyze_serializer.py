from rest_framework.serializers import ModelSerializer
from ..models import ImageForAnalyzes


class ImageForAnlyzeSerializer(ModelSerializer):
    class Meta:
        model = ImageForAnalyzes
        fields = (
            "image",
            "description",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "created_at": {"required": False},
            "updated_at": {"required": False},
        }
