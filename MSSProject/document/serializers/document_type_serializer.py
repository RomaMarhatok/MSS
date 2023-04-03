from rest_framework.serializers import ModelSerializer
from ..models import DocumentType


class DocumentTypeSerializer(ModelSerializer):
    class Meta:
        fields = (
            "name",
            "slug",
        )
        model = DocumentType
        extra_kwargs = {
            "slug": {"required": False},
        }
