import pytest
from userApp.serializers.user_document_doctor_serializer import (
    UserDocumentDoctorSerializer,
)


@pytest.mark.django_db
def test_deserializer(factory_user_document_doctor_fixture):
    serializer = UserDocumentDoctorSerializer(
        instance=factory_user_document_doctor_fixture
    )
    assert isinstance(serializer.data, dict)
