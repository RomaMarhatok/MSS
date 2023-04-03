import pytest

from doctor.serializers.doctor_serializer import DoctorSerializer
from doctor.models import Doctor


# user app imports
from user.serializers.role_serializer import RoleSerializer
from user.serializers.user_serializer import UserSerializer


@pytest.mark.django_db
def test_serialization(doctor_fixture):

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
    assert hasattr(instance.user, "role")


@pytest.mark.django_db
def test_multiply_serialization(factory_doctor_fixture):
    serializer = DoctorSerializer(
        instance=[factory_doctor_fixture, factory_doctor_fixture], many=True
    )
    assert isinstance(serializer.data, list)


@pytest.mark.django_db
def test_deserialization(factory_doctor_fixture):
    serializer = DoctorSerializer(instance=factory_doctor_fixture)
    assert isinstance(serializer.data, dict)
