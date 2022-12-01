import pytest
from userApp.serializers.patient_serializer import PatientSerializer
from userApp.serializers.user_serializer import UserSerializer
from userApp.serializers.role_serializer import RoleSerializer
from userApp.models import Patient


@pytest.mark.django_db
def test_serialize(patient_fixture):

    role_serializer = RoleSerializer(data=patient_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=patient_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()

    serializer = PatientSerializer(data=patient_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()

    assert Patient.objects.all().count()
    assert isinstance(instance, Patient)


@pytest.mark.django_db
def test_deserialize(factory_patient_fixture):
    serializer = PatientSerializer(instance=factory_patient_fixture)
    assert isinstance(serializer.data, dict)
    assert "user" in serializer.data
