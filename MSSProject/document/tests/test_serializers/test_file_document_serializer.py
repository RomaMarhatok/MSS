import pytest
from document.serializers import DocumentTypeSerializer, FileDocumentSerializer
from document.models import FileDocument, DocumentType
from user.models import User, Role
from user.serializers import UserSerializer
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor


@pytest.mark.django_db
def test_serilaization(file_document_fixture):
    Role.objects.create(name=Role.PATIENT)
    Role.objects.create(name=Role.DOCTOR)

    serializer = DocumentTypeSerializer(data=file_document_fixture["document_type"])
    assert serializer.is_valid(raise_exception=True)
    dt = serializer.save()
    file_document_fixture["document_type_slug"] = dt.slug

    user_serializer = UserSerializer(data=file_document_fixture["user"])
    assert user_serializer.is_valid(raise_exception=True)
    user = user_serializer.save()
    file_document_fixture["user_slug"] = user.slug

    user_serializer = UserSerializer(data=file_document_fixture["creator"]["user"])
    assert user_serializer.is_valid(raise_exception=True)
    doctor_user = user_serializer.save()
    file_document_fixture["creator"]["user_slug"] = doctor_user.slug
    file_document_fixture["creator_slug"] = doctor_user.slug

    doctor_serializer = DoctorSerializer(data=file_document_fixture["creator"])
    assert doctor_serializer.is_valid(raise_exception=True)
    doctor_serializer.save()

    document_serializer = FileDocumentSerializer(data=file_document_fixture)
    assert document_serializer.is_valid(raise_exception=True)
    instance: FileDocument = document_serializer.save()
    assert FileDocument.objects.all().count() == 1
    assert DocumentType.objects.count() == 1
    assert User.objects.all().count() == 2
    assert isinstance(instance, FileDocument)


@pytest.mark.django_db
def test_deserialization(factory_file_document_fixture):
    serializer = FileDocumentSerializer(instance=factory_file_document_fixture)
    assert isinstance(serializer.data, dict)
