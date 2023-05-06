from typing import OrderedDict
from rest_framework import serializers
from ..models import FileDocument, DocumentType
from user.models import User
from doctor.models import Doctor


class FileDocumentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    user_slug = serializers.SlugField(source="user.slug")
    creator_slug = serializers.SlugField(source="creator.user.slug")
    document_type_slug = serializers.SlugField(source="document_type.slug")

    class Meta:
        model = FileDocument
        fields = (
            "name",
            "slug",
            "document",
            "user_slug",
            "creator_slug",
            "document_type_slug",
        )

    def get_name(self, instance: FileDocument):
        return instance.name

    def get_slug(self, instance: FileDocument):
        return instance.slug

    def create(self, validated_data: OrderedDict) -> FileDocument:
        user = User.objects.get(slug=validated_data["user"]["slug"])
        document_type = DocumentType.objects.get(
            slug=validated_data["document_type"]["slug"]
        )
        creator = Doctor.objects.get(
            user__slug=validated_data["creator"]["user"]["slug"]
        )
        instance = FileDocument.objects.create(
            document=validated_data["document"],
            user=user,
            document_type=document_type,
            creator=creator,
        )
        return instance
