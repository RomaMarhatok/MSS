import pytest
from document.models import Document, DocumentType
from document.serializers.document_serializer import DocumentSerializer
from document.serializers.document_type_serializer import DocumentTypeSerializer

# user app imports
from user.serializers.user_serializer import UserSerializer
from user.models import User, Role

# doctor app imports
from doctor.serializers import DoctorSerializer


@pytest.mark.django_db
def test_serialization(document_fixture):

    serializer = DocumentTypeSerializer(data=document_fixture["document_type"])
    assert serializer.is_valid(raise_exception=True)
    dt = serializer.save()
    document_fixture["document_type_slug"] = dt.slug

    Role.objects.create(name=Role.PATIENT)
    Role.objects.create(name=Role.DOCTOR)

    user_serializer = UserSerializer(data=document_fixture["user"])
    assert user_serializer.is_valid(raise_exception=True)
    user = user_serializer.save()
    document_fixture["user_slug"] = user.slug

    user_serializer = UserSerializer(data=document_fixture["creator"]["user"])
    assert user_serializer.is_valid(raise_exception=True)
    doctor_user = user_serializer.save()
    document_fixture["creator"]["user_slug"] = doctor_user.slug
    document_fixture["creator_slug"] = doctor_user.slug

    doctor_serializer = DoctorSerializer(data=document_fixture["creator"])
    assert doctor_serializer.is_valid(raise_exception=True)
    doctor_serializer.save()
    document_serializer = DocumentSerializer(data=document_fixture)
    assert document_serializer.is_valid(raise_exception=True)
    instance = document_serializer.save()
    assert Document.objects.all().count() == 1
    assert DocumentType.objects.count() == 1
    assert User.objects.all().count() == 2
    assert isinstance(instance, Document)


@pytest.mark.django_db
def test_deserialization(factory_document_fixture):
    serializer = DocumentSerializer(instance=factory_document_fixture)
    assert isinstance(serializer.data, dict)
    assert "document_type" in serializer.data
    assert "slug" in serializer.data
    assert isinstance(serializer.data["document_type"], dict)
