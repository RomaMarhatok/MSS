import pytest
from user.serializers.user_serializer import UserSerializer
from user.serializers.role_serializer import RoleSerializer
from user.serializers.user_location_serializer import UserLocationSerializer
from user.models import UserLocation


@pytest.mark.django_db
def test_serialization(user_location_fixture):
    role_serializer = RoleSerializer(data=user_location_fixture["user"]["role"])
    assert role_serializer.is_valid(raise_exception=True)
    role_serializer.save()
    user_serializer = UserSerializer(data=user_location_fixture["user"])
    assert user_serializer.is_valid(raise_exception=True)
    user_serializer.save()

    user_location_serializer = UserLocationSerializer(data=user_location_fixture)
    assert user_location_serializer.is_valid(raise_exception=True)
    instance = user_location_serializer.save()
    assert UserLocation.objects.count() == 1
    assert isinstance(instance, UserLocation)


@pytest.mark.django_db
def test_deserialization(factory_user_location_fixture):
    serializer = UserLocationSerializer(instance=factory_user_location_fixture)
    assert isinstance(serializer.data, dict)
    assert "user" not in serializer.data
