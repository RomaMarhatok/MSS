from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import DocumentType


class DocumentTypeSerializer(ModelSerializer):
    slug = SerializerMethodField()

    class Meta:
        fields = (
            "name",
            "slug",
        )
        model = DocumentType

    def get_slug(self, instance: DocumentType):
        return instance.slug
