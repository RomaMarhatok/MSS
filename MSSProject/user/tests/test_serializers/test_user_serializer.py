import pytest
from common.utils.string_utils import generate_valid_login, generate_valid_password
from rest_framework.serializers import ValidationError
from user.models import Role, User
from user.serializers.user_serializer import UserSerializer


@pytest.mark.django_db
def test_serialization(patient_fixture):
    Role.objects.create(name=Role.PATIENT)
    serializer = UserSerializer(data=patient_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert len(serializer.errors) == 0
    assert User.objects.all().count() == 1
    assert isinstance(instance, User)


@pytest.mark.django_db
def test_serialization_without_role(patient_fixture):
    Role.objects.create(name=Role.PATIENT)
    serializer = UserSerializer(data=patient_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert len(serializer.errors) == 0
    assert User.objects.all().count() == 1
    assert isinstance(instance, User)


@pytest.mark.django_db
def test_update_serialization(patient_fixture):
    Role.objects.create(name=Role.PATIENT)
    serializer = UserSerializer(data=patient_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    patient_fixture["login"] = "asdk82hiwh89"
    serializer = UserSerializer(instance=instance, data=patient_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance2 = serializer.save()
    assert instance2.login == patient_fixture["login"]


@pytest.mark.django_db
def test_password_validator(patient_fixture):
    patient_fixture.pop("role")
    Role.objects.create(name=Role.PATIENT)
    patient_fixture["password"] = "1"
    serializer = UserSerializer(data=patient_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)
    patient_fixture["password"] = "#dmaskldm^_"
    serializer = UserSerializer(data=patient_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_login_validator(patient_fixture):
    Role.objects.create(name=Role.PATIENT)
    patient_fixture["login"] = ""
    serializer = UserSerializer(data=patient_fixture)
    serializer.is_valid()
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)
    patient_fixture["login"] = "#dmaskldm^_"
    serializer = UserSerializer(data=patient_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_login_password_serialization():
    Role.objects.create(name=Role.PATIENT)
    login = generate_valid_login()
    password = generate_valid_password()
    serializer = UserSerializer(data={"login": login, "password": password})
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert len(serializer.errors) == 0
    assert User.objects.all().count() == 1
    assert isinstance(instance, User)


@pytest.mark.django_db
def test_deserialization(factory_user_with_role_patient_fixture):
    serializer = UserSerializer(instance=factory_user_with_role_patient_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != "default"
    assert serializer.data["slug"] != ""


@pytest.mark.django_db
def test_filter(patient_fixture):
    Role.objects.create(name=Role.PATIENT)
    serializer = UserSerializer(data=patient_fixture)
    assert serializer.is_valid(raise_exception=True)
    serializer.save()
    patient_fixture.pop("role")
    assert User.objects.filter(**patient_fixture).exists()
    assert bool(User.objects.get(**patient_fixture))
