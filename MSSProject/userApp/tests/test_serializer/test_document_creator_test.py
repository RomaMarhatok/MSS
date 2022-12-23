import pytest
from userApp.serializers.document_creator_serializer import (
    DocumentCreatorSerializer,
)


@pytest.mark.django_db
def test_deserializer(factory_document_creator_fixture):
    serializer = DocumentCreatorSerializer(instance=factory_document_creator_fixture)
    assert isinstance(serializer.data, dict)
