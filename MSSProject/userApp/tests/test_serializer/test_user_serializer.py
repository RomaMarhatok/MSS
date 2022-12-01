import pytest
from userApp.serializers.user_serializer import UserSerializer
from userApp.models import User, Role


@pytest.mark.django_db
def test_serialization(user_fixture):
    Role.objects.create(**user_fixture["role"])
    serializer = UserSerializer(data=user_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert len(serializer.errors) == 0
    assert User.objects.all().count() == 1
    assert isinstance(instance, User)


@pytest.mark.django_db
def test_deserialization(factory_user_fixture):
    serializer = UserSerializer(instance=factory_user_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != "default"
    assert serializer.data["slug"] != ""
