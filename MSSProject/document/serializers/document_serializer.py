from rest_framework.serializers import ModelSerializer, SlugField
from typing import OrderedDict
from ..models import Document, DocumentType
from .document_type_serializer import DocumentTypeSerializer
from common.utils.date_utils import parse_date_iso_format

# user app import
from user.models import User

# doctor app import
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor


class DocumentSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")
    document_type = DocumentTypeSerializer(many=False, required=True)
    creator = DoctorSerializer(many=False, required=True)

    class Meta:
        model = Document
        fields = (
            "name",
            "slug",
            "user_slug",
            "creator",
            "content",
            "document_type",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "document_type": {"validators": []},
            "creator": {"validators": []},
            "name": {"validators": []},
            "slug": {"required": False},
            "created_at": {"required": False},
            "updated_at": {"required": False},
        }

    def create(self, validated_data: OrderedDict) -> Document:
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        document_type = DocumentType.objects.get(
            name=validated_data["document_type"]["name"]
        )
        validated_data.pop("document_type")
        creator = Doctor.objects.get(
            user__login=validated_data["creator"]["user"]["login"]
        )
        validated_data.pop("creator")
        instance = Document.objects.create(
            **validated_data, user=user, document_type=document_type, creator=creator
        )
        return instance

    def to_representation(self, instance: Document):
        rep = super().to_representation(instance)

        if "repr" in self.context and self.context["repr"] == "list":
            rep.pop("content")
            rep.pop("creator")

        rep["created_at"] = parse_date_iso_format(rep["created_at"])
        rep["updated_at"] = parse_date_iso_format(rep["updated_at"])
        rep["document_type"]["name"] = rep["document_type"]["name"].lower().capitalize()
        rep["creator"] = {
            "full_name": instance.creator.user.userpersonalinfo.full_name,
            "creator_slug": instance.creator.user.slug,
        }
        return rep
