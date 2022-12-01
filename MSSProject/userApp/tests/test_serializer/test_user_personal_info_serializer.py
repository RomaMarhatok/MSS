import pytest
from userApp.models import UserPersonalInfo
from userApp.serializers.user_serializer import (
    UserPersonalInfoSerializer,
    UserSerializer,
)
from userApp.serializers.role_serializer import RoleSerializer


@pytest.mark.django_db
def test_serialize(user_personal_info_with_image_fixture):
    role_serializer = RoleSerializer(
        data=user_personal_info_with_image_fixture["user"]["role"]
    )
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_personal_info_with_image_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()

    serializer = UserPersonalInfoSerializer(data=user_personal_info_with_image_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert UserPersonalInfo.objects.all().count() == 1
    assert isinstance(instance, UserPersonalInfo)


@pytest.mark.django_db
def test_deserialize(factory_user_personal_info_fixture):
    serializer = UserPersonalInfoSerializer(instance=factory_user_personal_info_fixture)
    assert isinstance(serializer.data, dict)