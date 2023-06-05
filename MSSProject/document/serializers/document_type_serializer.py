from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import DocumentType


class DocumentTypeSerializer(ModelSerializer):
    slug = SerializerMethodField()
    unicode_name = SerializerMethodField()

    class Meta:
        fields = (
            "name",
            "slug",
            "unicode_name",
        )
        model = DocumentType

    def get_slug(self, instance: DocumentType):
        return instance.slug

    def get_unicode_name(self, instance: DocumentType):
        return instance.unicode_name

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["name"] = rep["name"].lower().capitalize()
        return rep
