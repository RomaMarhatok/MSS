import pytest
from userApp.serializers.user_serializer import UserSerializer
from userApp.models import User, Role
from rest_framework.serializers import ValidationError


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
def test_serialization_without_role(user_fixture):
    user_fixture.pop("role")
    Role.objects.create(name="patient")
    serializer = UserSerializer(data=user_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert len(serializer.errors) == 0
    assert User.objects.all().count() == 1
    assert isinstance(instance, User)


@pytest.mark.django_db
def test_update_serialization(user_fixture):
    user_fixture.pop("role")
    Role.objects.create(name="patient")
    serializer = UserSerializer(data=user_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    user_fixture["login"] = "asdk82hiwh89"
    serializer = UserSerializer(instance=instance, data=user_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance2 = serializer.save()
    assert instance2.login == user_fixture["login"]


@pytest.mark.django_db
def test_password_validator(user_fixture):
    user_fixture.pop("role")
    Role.objects.create(name="patient")
    user_fixture["password"] = "1"
    serializer = UserSerializer(data=user_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)
    user_fixture["password"] = "#dmaskldm^_"
    serializer = UserSerializer(data=user_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_login_validator(user_fixture):
    user_fixture.pop("role")
    Role.objects.create(name="patient")
    user_fixture["login"] = ""
    serializer = UserSerializer(data=user_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)
    user_fixture["login"] = "#dmaskldm^_"
    serializer = UserSerializer(data=user_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_deserialization(factory_user_fixture):
    serializer = UserSerializer(instance=factory_user_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != "default"
    assert serializer.data["slug"] != ""
