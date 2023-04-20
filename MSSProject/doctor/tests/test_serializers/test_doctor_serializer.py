import pytest

from doctor.serializers.doctor_serializer import DoctorSerializer
from doctor.models import Doctor


# user app imports
from user.models import Role
from user.serializers.user_serializer import UserSerializer


@pytest.mark.django_db
def test_serialization(doctor_fixture):

    Role.objects.create(name=Role.PATIENT)

    user_serializer = UserSerializer(data=doctor_fixture["user"])
    assert user_serializer.is_valid()
    user = user_serializer.save()
    doctor_fixture["user_slug"] = user.slug
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
