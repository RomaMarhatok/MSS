import pytest
import random
from document.serializers.document_type_serializer import DocumentTypeSerializer
from document.models import DocumentType


@pytest.mark.django_db
def test_serialization(document_type_fixture):
    serializer = DocumentTypeSerializer(data=document_type_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert DocumentType.objects.all().count() == 1
    assert isinstance(instance, DocumentType)


@pytest.mark.django_db
def test_serialization_with_choices(document_type_fixture):
    document_type_fixture["name"] = random.choice(DocumentType.DOCUMENT_TYPE_CHOICES)[0]
    serializer = DocumentTypeSerializer(data=document_type_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert DocumentType.objects.all().count() == 1
    assert isinstance(instance, DocumentType)


@pytest.mark.django_db
def test_deserialization(factory_document_type_fixture):
    serializer = DocumentTypeSerializer(instance=factory_document_type_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert "name" in serializer.data
