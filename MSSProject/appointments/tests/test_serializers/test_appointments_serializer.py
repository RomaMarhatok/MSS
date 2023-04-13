import pytest
from appointments.models import Appointments
from appointments.serializers import AppointmentsSerializer

# user app imports
from user.serializers import UserSerializer
from user.models import Role

# doctor app imports
from doctor.serializers import DoctorSerializer, DoctorSpecializationSerializer


@pytest.mark.django_db
def test_serialization(appoitment_fixture):
    Role.objects.create(name=Role.PATIENT)
    Role.objects.create(name=Role.DOCTOR)

    serializer = DoctorSpecializationSerializer(
        data=appoitment_fixture["doctor_specialization"]
    )
    assert serializer.is_valid(raise_exception=True)
    doctor_specialization = serializer.save()
    appoitment_fixture["doctor_specialization_slug"] = doctor_specialization.slug

    serializer = UserSerializer(data=appoitment_fixture["patient"])
    assert serializer.is_valid(raise_exception=True)
    user = serializer.save()
    appoitment_fixture["patient_slug"] = user.slug

    serializer = UserSerializer(data=appoitment_fixture["doctor"]["user"])
    assert serializer.is_valid(raise_exception=True)
    user = serializer.save()
    appoitment_fixture["doctor"]["user_slug"] = user.slug

    serializer = DoctorSerializer(data=appoitment_fixture["doctor"])
    assert serializer.is_valid(raise_exception=True)
    serializer.save()

    serializer = AppointmentsSerializer(data=appoitment_fixture)
    assert serializer.is_valid(raise_exception=True)
    serializer.save()

    assert Appointments.objects.count() == 1


@pytest.mark.django_db
def test_deserializaition(factory_appointments_fixture):
    serializer = AppointmentsSerializer(instance=factory_appointments_fixture)
    assert isinstance(serializer.data, dict)
