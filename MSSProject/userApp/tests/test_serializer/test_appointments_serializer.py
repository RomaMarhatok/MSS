import pytest
from userApp.serializers.appointments_serializer import AppointmentsSerializer
from userApp.serializers.role_serializer import RoleSerializer
from userApp.serializers.user_serializer import UserSerializer
from userApp.serializers.doctor_serializer import DoctorSerializer
from userApp.serializers.patient_serializer import PatientSerializer
from userApp.models import Appointments


@pytest.mark.django_db
def test_serialize(appoitment_fixture):
    serializer = RoleSerializer(data=appoitment_fixture["doctor"]["user"]["role"])
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=appoitment_fixture["doctor"]["user"])
    assert serializer.is_valid()
    serializer.save()

    serializer = RoleSerializer(data=appoitment_fixture["patient"]["user"]["role"])
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=appoitment_fixture["patient"]["user"])
    assert serializer.is_valid()
    serializer.save()

    serializer = DoctorSerializer(data=appoitment_fixture["doctor"])
    assert serializer.is_valid()
    serializer.save()

    serializer = PatientSerializer(data=appoitment_fixture["patient"])
    assert serializer.is_valid()
    serializer.save()

    serializer = AppointmentsSerializer(data=appoitment_fixture)
    assert serializer.is_valid()
    serializer.save()

    assert Appointments.objects.count() == 1


@pytest.mark.django_db
def test_deserialize(factory_appointments_fixture):
    serializer = AppointmentsSerializer(instance=factory_appointments_fixture)
    assert isinstance(serializer.data, dict)
