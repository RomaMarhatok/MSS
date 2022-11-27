from rest_framework.serializers import ModelSerializer

from .models import DocumentType, Roles, User, UserDocument, UserPersonalInfo


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = ("name",)


class DocumentTypeSerializer(ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ("document_type",)


class UserSerializer(ModelSerializer):
    role = RolesSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ("username", "login", "password", "role")


class UserPersonalInfoSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = UserPersonalInfo
        fields = ("user", "image", "first_name", "second_name", "patronymic", "email")


class UserDocumentSerializer(ModelSerializer):
    user = UserSerializer(many=False, required=True)
    doctype = DocumentTypeSerializer(many=False, required=True)

    class Meta:
        model = UserDocument
        fields = ("user", "content", "doctype")
