import pytest
from userApp.models import Document, User, DocumentType
from userApp.serializers.user_serializer import UserSerializer
from userApp.serializers.document_serializer import DocumentSerializer
from userApp.serializers.document_type_serializer import DocumentTypeSerializer
from userApp.serializers.role_serializer import RoleSerializer


@pytest.mark.django_db
def test_serialization(document_fixture):

    serializer = DocumentTypeSerializer(data=document_fixture["document_type"])
    assert serializer.is_valid()
    serializer.save()

    role_serializer = RoleSerializer(data=document_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=document_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()

    user_document_serializer = DocumentSerializer(data=document_fixture)
    assert user_document_serializer.is_valid(raise_exception=True)
    instance = user_document_serializer.save()
    assert Document.objects.all().count() == 1
    assert DocumentType.objects.count() == 1
    assert User.objects.all().count() == 1
    assert isinstance(instance, Document)


@pytest.mark.django_db
def test_desrialization(factory_document_fixture):
    serializer = DocumentSerializer(instance=factory_document_fixture)
    assert isinstance(serializer.data, dict)
    assert "document_type" in serializer.data
    assert "slug" in serializer.data
    assert isinstance(serializer.data["document_type"], dict)
