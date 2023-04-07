from django.http import HttpRequest
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import ImageForAnalyzes


class ImageForAnlyzeSerializer(ModelSerializer):
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()

    class Meta:
        model = ImageForAnalyzes
        fields = (
            "image",
            "description",
            "created_at",
            "updated_at",
        )

    def get_created_at(self, instance: ImageForAnalyzes):
        return instance.created_at

    def get_updated_at(self, instance: ImageForAnalyzes):
        return instance.updated_at

    def to_representation(self, instance: ImageForAnalyzes):
        rep = super().to_representation(instance)
        try:
            if (
                instance.image.storage.exists(instance.image.name)
                and "request" in self.context
            ):
                request: HttpRequest = self.context["request"]
                rep["image"] = request.build_absolute_uri(instance.image.url)
            else:
                rep["image"] = "https://placehold.co/400"
        except ValueError:
            rep.pop("image")
        return rep
