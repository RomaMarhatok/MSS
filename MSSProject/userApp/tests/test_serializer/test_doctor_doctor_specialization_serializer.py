import pytest
from userApp.serializers.doctor_doctor_specialization_serializer import (
    DoctorDoctorSpecializationSerializer,
)

from userApp.models import DoctorDoctorSpecialization


@pytest.mark.django_db
def test_serializer(factory_doctor_fixture, factory_doctor_specialization_fixture):
    serializer = DoctorDoctorSpecializationSerializer(
        data={
            "doctor": factory_doctor_fixture.pk,
            "doctor_specialization": factory_doctor_specialization_fixture.pk,
        }
    )
    assert serializer.is_valid()
    instance = serializer.save()
    assert DoctorDoctorSpecialization.objects.all().count() == 1
    assert isinstance(instance, DoctorDoctorSpecialization)


@pytest.mark.django_db
def test_deserializer(factory_doctor_doctor_specialization_fixture):
    serializer = DoctorDoctorSpecializationSerializer(
        instance=factory_doctor_doctor_specialization_fixture
    )
    assert isinstance(serializer.data, dict)
