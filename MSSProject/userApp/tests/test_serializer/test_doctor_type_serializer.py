import pytest
from userApp.serializers.doctor_type_serializer import DoctorTypeSerializer
from userApp.models import DoctorType


@pytest.mark.django_db
def test_serialization(doctor_type_fixture):
    serializer = DoctorTypeSerializer(data=doctor_type_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert isinstance(instance, DoctorType)
    assert hasattr(instance, "slug")
    assert instance.slug != "default"
    assert instance.slug != ""


@pytest.mark.django_db
def test_desrialization(factory_doctor_type_fixture):
    serializer = DoctorTypeSerializer(instance=factory_doctor_type_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != "default"
    assert serializer.data["slug"] != ""
