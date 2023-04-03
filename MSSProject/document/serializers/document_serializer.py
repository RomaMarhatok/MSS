from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import Document, DocumentType
from .document_type_serializer import DocumentTypeSerializer
from common.utils.date_utils import parse_date_iso_format

# user app import
from user.serializers import UserSerializer
from user.models import User

# doctor app import
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor


class DocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)
    document_type = DocumentTypeSerializer(many=False, required=True)
    creator = DoctorSerializer(many=False, required=True)

    class Meta:
        model = Document
        fields = (
            "name",
            "slug",
            "user",
            "creator",
            "content",
            "document_type",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "user": {"validators": [], "lookup_field": "slug"},
            "document_type": {"validators": []},
            "creator": {"validators": []},
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
        creator = Doctor.objects.get(
            user__login=validated_data["creator"]["user"]["login"]
        )
        validated_data.pop("creator")
        instance, _ = Document.objects.get_or_create(
            **validated_data, user=user, document_type=document_type, creator=creator
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("user")
        if "include_context" in self.context and not self.context["include_context"]:
            rep.pop("content")
        rep["created_at"] = parse_date_iso_format(rep["created_at"])
        rep["updated_at"] = parse_date_iso_format(rep["updated_at"])
        rep["document_type"]["name"] = rep["document_type"]["name"].lower().capitalize()
        return rep