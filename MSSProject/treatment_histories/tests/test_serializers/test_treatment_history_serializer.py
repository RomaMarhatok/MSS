import pytest
from treatment_histories.serializers import TreatmentHistorySerializer
from treatment_histories.models import TreatmentHistory

from user.serializers import UserSerializer
from user.models import Role

from doctor.serializers import DoctorSerializer


@pytest.mark.django_db
def test_serialization(treatment_history_fixture):
    Role.objects.create(name=Role.PATIENT)
    Role.objects.create(name=Role.DOCTOR)

    serializer = UserSerializer(data=treatment_history_fixture["doctor"]["user"])
    assert serializer.is_valid(raise_exception=True)
    user = serializer.save()
    treatment_history_fixture["doctor"]["user_slug"] = user.slug

    serializer = DoctorSerializer(data=treatment_history_fixture["doctor"])
    assert serializer.is_valid(raise_exception=True)
    doctor = serializer.save()
    treatment_history_fixture["doctor_slug"] = doctor.user.slug

    serializer = UserSerializer(data=treatment_history_fixture["patient"])
    assert serializer.is_valid(raise_exception=True)
    user = serializer.save()
    treatment_history_fixture["patient_slug"] = user.slug

    serializer = TreatmentHistorySerializer(data=treatment_history_fixture)
    assert serializer.is_valid(raise_exception=True)
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
