import pytest
from userApp.serializers.user_serializer import UserDocumentTypeSerializer
from userApp.models import UserDocumentType


@pytest.mark.django_db
def test_serialize(user_document_type_fixture):
    serializer = UserDocumentTypeSerializer(data=user_document_type_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert UserDocumentType.objects.all().count() == 1
    assert isinstance(instance, UserDocumentType)


@pytest.mark.django_db
def test_deserialize(factory_user_document_type_fixture):
    serializer = UserDocumentTypeSerializer(instance=factory_user_document_type_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert "name" in serializer.data
