import pytest
from userApp.models import UserDocument, User
from userApp.serializers.user_serializer import UserDocumentSerializer, UserSerializer
from userApp.serializers.role_serializer import RoleSerializer


@pytest.mark.django_db
def test_serialization(user_document_fixture):

    role_serializer = RoleSerializer(data=user_document_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_document_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()

    user_document_serializer = UserDocumentSerializer(data=user_document_fixture)
    assert user_document_serializer.is_valid()
    instance = user_document_serializer.save()
    assert UserDocument.objects.all().count() == 1
    assert User.objects.all().count() == 1
    assert isinstance(instance, UserDocument)


@pytest.mark.django_db
def test_desrialization(factory_user_docuemnt_fixture):
    serializer = UserDocumentSerializer(instance=factory_user_docuemnt_fixture)
    assert isinstance(serializer.data, dict)
    assert "user" in serializer.data
    assert isinstance(serializer.data["user"], dict)
    assert "slug" in serializer.data
    assert isinstance(serializer.data["slug"], str)
