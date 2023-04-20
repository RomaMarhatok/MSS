import pytest
from django.utils.text import slugify
from document.serializers.document_type_serializer import DocumentTypeSerializer
from document.models import DocumentType
from unidecode import unidecode


@pytest.mark.django_db
def test_serialization(document_type_fixture):
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
