import pytest
from appointments.models import Appointments
from appointments.serializers import AppointmentsSerializer

# user app imports
from user.serializers import RoleSerializer, UserSerializer

# doctor app imports
from doctor.serializers import DoctorSerializer, DoctorSpecializationSerializer


@pytest.mark.django_db
def test_serialization(appoitment_fixture):
    serializer = DoctorSpecializationSerializer(
        data=appoitment_fixture["doctor_specialization"]
    )
    assert serializer.is_valid()
    doctor_specialization = serializer.save()
    appoitment_fixture["doctor_specialization"]["slug"] = doctor_specialization.slug
    serializer = RoleSerializer(data=appoitment_fixture["doctor"]["user"]["role"])
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=appoitment_fixture["doctor"]["user"])
    assert serializer.is_valid()
    serializer.save()

    serializer = RoleSerializer(data=appoitment_fixture["patient"]["role"])
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=appoitment_fixture["patient"])
    assert serializer.is_valid()
    serializer.save()

    serializer = DoctorSerializer(data=appoitment_fixture["doctor"])
    assert serializer.is_valid()
    serializer.save()

    serializer = AppointmentsSerializer(data=appoitment_fixture)
    assert serializer.is_valid(raise_exception=True)
    serializer.save()

    assert Appointments.objects.count() == 1


@pytest.mark.django_db
def test_deserializaition(factory_appointments_fixture):
    serializer = AppointmentsSerializer(instance=factory_appointments_fixture)
    assert isinstance(serializer.data, dict)
    assert serializer.data["doctor"]["user"]["full_name"] is None or isinstance(
        serializer.data["doctor"]["user"]["full_name"], str
    )
    serializer = AppointmentsSerializer(
        instance=factory_appointments_fixture, context={"is_doctor": True}
    )
    assert isinstance(serializer.data, dict)
    assert serializer.data["patient"]["full_name"] is None or isinstance(
        serializer.data["patient"]["full_name"], str
    )
