from django.http import HttpRequest
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)
from ..models import ImageForAnalyzes
from common.utils.string_utils import generate_hash_from_string


class ImageForAnlyzeSerializer(ModelSerializer):
    slug = SerializerMethodField()
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()

    class Meta:
        model = ImageForAnalyzes
        fields = (
            "slug",
            "image",
            "description",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {"image": {"validators": []}}

    def get_slug(self, instance: ImageForAnalyzes):
        return instance.slug

    def validate_image(self, value: InMemoryUploadedFile):
        name = generate_hash_from_string(value.name.split(".")[0])[:51]
        for image_name in ImageForAnalyzes.objects.values_list("image", flat=True):
            if name == image_name.split("/")[-1].split("_")[0]:
                message = "Изображение с таким именем уже существует"
                raise ValidationError(message)
        return value

    def get_created_at(self, instance: ImageForAnalyzes):
        return instance.created_at

    def get_updated_at(self, instance: ImageForAnalyzes):
        return instance.updated_at

    def create(self, validated_data):
        return ImageForAnalyzes.objects.create(**validated_data)

    def to_representation(self, instance: ImageForAnalyzes):
        rep = super().to_representation(instance)
        if (
            instance.image.storage.exists(instance.image.name)
            and "request" in self.context
        ):
            request: HttpRequest = self.context["request"]
            rep["image"] = request.build_absolute_uri(instance.image.url)
        else:
            rep["image"] = "https://placehold.co/400"
        return rep
