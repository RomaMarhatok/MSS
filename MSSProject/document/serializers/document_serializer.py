from rest_framework.serializers import ModelSerializer, SlugField, SerializerMethodField
from typing import OrderedDict
from ..models import Document, DocumentType
from .document_type_serializer import DocumentTypeSerializer


# user app import
from user.models import User, UserPersonalInfo

# doctor app import
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor


class DocumentSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")
    document_type = DocumentTypeSerializer(many=False, required=True)
    creator = DoctorSerializer(many=False, required=True)
    slug = SerializerMethodField()
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()

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
        }

    def get_slug(self, instance: Document):
        return instance.slug

    def get_created_at(self, instance: Document):
        return instance.created_at

    def get_updated_at(self, instance: Document):
        return instance.updated_at

    def create(self, validated_data: OrderedDict) -> Document:
        user = User.objects.get(slug=validated_data["user"]["slug"])
        validated_data.pop("user")
        # change on slug
        document_type = DocumentType.objects.get(
            name=validated_data["document_type"]["name"]
        )
        validated_data.pop("document_type")
        creator = Doctor.objects.get(
            user__slug=validated_data["creator"]["user"]["slug"]
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

        rep["document_type"]["name"] = rep["document_type"]["name"].lower().capitalize()
        rep["creator"] = {
            "creator_slug": instance.creator.user.slug,
        }
        try:
            rep["creator"]["full_name"] = (
                instance.creator.user.userpersonalinfo.full_name,
            )
        except UserPersonalInfo.DoesNotExist:
            rep["creator"]["full_name"] = ""
        return rep
