from rest_framework.serializers import ModelSerializer
from ..models import ImageForAnalyzes
from django.core.handlers.wsgi import WSGIRequest


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

    def to_representation(self, instance: ImageForAnalyzes):
        rep = super().to_representation(instance)
        if (
            instance.image.storage.exists(instance.image.name)
            and "request" in self.context
        ):
            request: WSGIRequest = self.context["request"]
            rep["image"] = request.build_absolute_uri(instance.image.url)
        return rep
