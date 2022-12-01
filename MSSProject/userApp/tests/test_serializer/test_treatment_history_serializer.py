import pytest
from userApp.serializers.treatment_history_serializer import TreatmentHistorySerializer
from userApp.models import TreatmentHistory
from userApp.serializers.doctor_serializer import DoctorSerializer
from userApp.serializers.patient_serializer import PatientSerializer
from userApp.serializers.user_serializer import UserSerializer
from userApp.serializers.role_serializer import RoleSerializer


@pytest.mark.django_db
def test_serialization(treatment_history_fixture):
    serializer = RoleSerializer(
        data=treatment_history_fixture["doctor"]["user"]["role"]
    )
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=treatment_history_fixture["doctor"]["user"])
    assert serializer.is_valid()
    serializer.save()

    serializer = DoctorSerializer(data=treatment_history_fixture["doctor"])
    assert serializer.is_valid()
    serializer.save()

    serializer = PatientSerializer(data=treatment_history_fixture["patient"])
    assert serializer.is_valid()
    serializer.save()

    serializer = TreatmentHistorySerializer(data=treatment_history_fixture)
    assert serializer.is_valid()
    instance = serializer.save()
    assert TreatmentHistory.objects.all().count() == 1
    assert isinstance(instance, TreatmentHistory)
    assert hasattr(instance, "slug")
    assert instance.slug != ""
    assert instance.slug != "default"


@pytest.mark.django_db
def test_deserialization(factory_treatment_history_fixture):
    serializer = TreatmentHistorySerializer(instance=factory_treatment_history_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != ""
    assert serializer.data["slug"] != "default"
    slug = (
        serializer.data["doctor"]["user"]["slug"]
        + serializer.data["patient"]["user"]["slug"]
    )
    assert serializer.data["slug"] == slug
