import pytest
from doctor.serializers.doctor_summary_serializer import DoctorSummarySerializer
from doctor.serializers.doctor_serializer import DoctorSerializer
from doctor.models import DoctorSummary

# user app imports
from user.serializers.role_serializer import RoleSerializer
from user.serializers.user_serializer import UserSerializer


@pytest.mark.django_db
def test_serialization(doctor_summary_fixture):
    role_serializer = RoleSerializer(
        data=doctor_summary_fixture["doctor"]["user"]["role"]
    )
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=doctor_summary_fixture["doctor"]["user"])
    assert user_serializer.is_valid()
    user_serializer.save()

    serializer = DoctorSerializer(data=doctor_summary_fixture["doctor"])
    assert serializer.is_valid(raise_exception=True)
    serializer.save()

    serializer = DoctorSummarySerializer(data=doctor_summary_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert isinstance(instance, DoctorSummary)
