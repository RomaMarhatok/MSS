import pytest
from userApp.serializers.role_serializer import RoleSerializer
from userApp.serializers.user_serializer import UserSerializer
from userApp.serializers.doctor_serializer import DoctorSerializer
from userApp.models import Doctor


@pytest.mark.django_db
def test_serialize(doctor_fixture):

    role_serializer = RoleSerializer(data=doctor_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=doctor_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()

    serializer = DoctorSerializer(data=doctor_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert Doctor.objects.all().count() == 1
    assert isinstance(instance, Doctor)
    assert hasattr(instance.user, "slug")
    assert instance.user.slug != ""
    assert instance.user.slug != "default"


@pytest.mark.django_db
def test_multiply_serialization(factory_doctor_fixture):
    serializer = DoctorSerializer(
        instance=[factory_doctor_fixture, factory_doctor_fixture], many=True
    )
    assert isinstance(serializer.data, list)


@pytest.mark.django_db
def test_deserialize(factory_doctor_fixture):
    serializer = DoctorSerializer(instance=factory_doctor_fixture)
    assert isinstance(serializer.data, dict)
    assert isinstance(serializer.data["doctor_types"], list)
    assert "slug" in serializer.data["user"]
    assert serializer.data["user"]["slug"] != "default"
    assert serializer.data["user"]["slug"] != ""
