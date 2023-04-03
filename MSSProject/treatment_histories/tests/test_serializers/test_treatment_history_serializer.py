import pytest
from treatment_histories.serializers import TreatmentHistorySerializer
from treatment_histories.models import TreatmentHistory

# user app imports
from user.serializers import UserSerializer, RoleSerializer
from user.models import User, Role

#
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor


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

    serializer = RoleSerializer(data=treatment_history_fixture["patient"]["role"])
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=treatment_history_fixture["patient"])
    assert serializer.is_valid()
    serializer.save()

    serializer = DoctorSerializer(data=treatment_history_fixture["doctor"])
    assert serializer.is_valid()
    serializer.save()

    serializer = UserSerializer(data=treatment_history_fixture["patient"])
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
