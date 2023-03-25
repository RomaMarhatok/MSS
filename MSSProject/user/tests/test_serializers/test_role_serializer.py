import pytest
from user.serializers.role_serializer import RoleSerializer
from user.models import Role


@pytest.mark.django_db
def test_serialization(patient_role_fixture):
    serializer = RoleSerializer(data=patient_role_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert Role.objects.all().count() == 1
    assert instance.name == Role.PATIENT


@pytest.mark.django_db
def test_deserialization(factory_patient_role_fixture):
    serializer = RoleSerializer(instance=factory_patient_role_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
