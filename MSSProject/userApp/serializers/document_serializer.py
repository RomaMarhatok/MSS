from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import Document, User, DocumentType
from .user_serializer import UserSerializer
from .document_type_serializer import DocumentTypeSerializer
from ..utils.date_utils import parse_date_iso_format
from ..models import DocumentCreator


class DocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)
    document_type = DocumentTypeSerializer(many=False, required=True)

    class Meta:
        model = Document
        fields = (
            "name",
            "slug",
            "user",
            "content",
            "document_type",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "user": {"validators": [], "lookup_field": "slug"},
            "document_type": {"validators": []},
            "name": {"validators": []},
            "slug": {"required": False},
            "created_at": {"required": False},
            "updated_at": {"required": False},
        }

    def create(self, validated_data: OrderedDict) -> Document:
        user = User.objects.get(login=validated_data["user"]["login"])
        validated_data.pop("user")
        document_type = DocumentType.objects.get(
            name=validated_data["document_type"]["name"]
        )
        validated_data.pop("document_type")
        instance, _ = Document.objects.get_or_create(
            **validated_data, user=user, document_type=document_type
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("user")
        if "include_context" in self.context and not self.context["include_context"]:
            rep.pop("content")
        rep["created_at"] = parse_date_iso_format(rep["created_at"])
        rep["updated_at"] = parse_date_iso_format(rep["updated_at"])
        return rep
