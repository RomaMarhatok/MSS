import pytest
from userApp.serializers.doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from userApp.models import DoctorSpecialization


@pytest.mark.django_db
def test_serialization(doctor_specialization_fixture):
    serializer = DoctorSpecializationSerializer(data=doctor_specialization_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert isinstance(instance, DoctorSpecialization)
    assert hasattr(instance, "slug")
    assert instance.slug != "default"
    assert instance.slug != ""


@pytest.mark.django_db
def test_desrialization(factory_doctor_specialization_fixture):
    serializer = DoctorSpecializationSerializer(
        instance=factory_doctor_specialization_fixture
    )
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != "default"
    assert serializer.data["slug"] != ""
