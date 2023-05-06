from typing import OrderedDict
from rest_framework.serializers import ModelSerializer, SlugField, SerializerMethodField
from common.utils.date_utils import parse_date_to_dict
from ..models import Document, DocumentType

from user.models import User
from doctor.models import Doctor


class DocumentSerializer(ModelSerializer):
    user_slug = SlugField(source="user.slug")
    document_type_slug = SlugField(source="document_type.slug")
    creator_slug = SlugField(source="creator.user.slug")
    slug = SerializerMethodField()
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()

    class Meta:
        model = Document
        fields = (
            "name",
            "slug",
            "user_slug",
            "creator_slug",
            "content",
            "document_type_slug",
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
        document_type = DocumentType.objects.get(
            slug=validated_data["document_type"]["slug"]
        )
        creator = Doctor.objects.get(
            user__slug=validated_data["creator"]["user"]["slug"]
        )
        instance = Document.objects.create(
            name=validated_data["name"],
            content=validated_data["content"],
            user=user,
            document_type=document_type,
            creator=creator,
        )
        return instance

    def update(self, instance: Document, validated_data):
        return Document.objects.filter(slug=instance.slug).update(
            name=validated_data["name"], content=validated_data["content"]
        )

    def to_representation(self, instance: Document):
        rep = super().to_representation(instance)
        if "repr" in self.context and self.context["repr"] == "list":
            rep.pop("content")

        rep["parsed_date"] = parse_date_to_dict(str(rep["created_at"]))
        rep["document_type"] = {
            "name": instance.document_type.name.lower().capitalize(),
            "slug": instance.document_type.slug,
        }
        rep["document_type_name"] = rep["document_type"]["name"]
        rep["creator"] = {
            "creator_slug": instance.creator.user.slug,
        }
        if hasattr(instance.creator.user, "userpersonalinfo"):
            rep["creator"][
                "full_name"
            ] = instance.creator.user.userpersonalinfo.full_name

        rep["patient"] = {"patient_slug": instance.user.slug}
        if hasattr(instance.user, "userpersonalinfo"):
            rep["patient"][
                "full_name"
            ] = instance.creator.user.userpersonalinfo.full_name
        if "document_type_slug" in rep:
            rep.pop("document_type_slug")
        return rep
