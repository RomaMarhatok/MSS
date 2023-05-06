import pytest
from physical.models import PhysicalParameters
from physical.serializers import (
    PhysicalParametersSerializer,
)


@pytest.mark.django_db
def test_serialize(factory_user_with_role_patient_fixture, physical_parameters_fixture):
    physical_parameters_fixture[
        "user_slug"
    ] = factory_user_with_role_patient_fixture.slug
    serializer = PhysicalParametersSerializer(data=physical_parameters_fixture)
    assert serializer.is_valid(raise_exception=True)
    serializer.save()
    assert PhysicalParameters.objects.count() == 1


@pytest.mark.django_db
def test_deserialization(factory_physical_parameters_fixture):
    serializer = PhysicalParametersSerializer(
        instance=factory_physical_parameters_fixture
    )
    assert isinstance(serializer.data, dict)
