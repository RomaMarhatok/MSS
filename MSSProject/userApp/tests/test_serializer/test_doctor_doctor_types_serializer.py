import pytest
from userApp.serializers.doctor_doctor_type_serializer import (
    DoctorDoctorTypesSerializer,
)

from userApp.models import DoctorDoctorTypes


@pytest.mark.django_db
def test_serializer(factory_doctor_fixture, factory_doctor_type_fixture):
    serializer = DoctorDoctorTypesSerializer(
        data={
            "doctor": factory_doctor_fixture.pk,
            "doctor_type": factory_doctor_type_fixture.pk,
        }
    )
    assert serializer.is_valid()
    instance = serializer.save()
    assert DoctorDoctorTypes.objects.all().count() == 1
    assert isinstance(instance, DoctorDoctorTypes)


@pytest.mark.django_db
def test_deserializer(factory_doctor_doctor_types_fixture):
    serializer = DoctorDoctorTypesSerializer(
        instance=factory_doctor_doctor_types_fixture
    )
    assert isinstance(serializer.data, dict)
