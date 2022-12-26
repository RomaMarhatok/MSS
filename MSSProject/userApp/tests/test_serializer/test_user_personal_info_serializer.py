import pytest
from userApp.models import UserPersonalInfo
from userApp.serializers.user_serializer import UserSerializer
from userApp.serializers.user_personal_info_serializer import UserPersonalInfoSerializer
from userApp.serializers.role_serializer import RoleSerializer
from rest_framework.validators import ValidationError


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
    instance: UserPersonalInfo = serializer.save()
    assert UserPersonalInfo.objects.all().count() == 1
    assert isinstance(instance, UserPersonalInfo)
    assert instance.image is not None


@pytest.mark.django_db
def test_serialize_without_fields(user_personal_info_with_image_fixture):
    role_serializer = RoleSerializer(
        data=user_personal_info_with_image_fixture["user"]["role"]
    )
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_personal_info_with_image_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()
    serializer = UserPersonalInfoSerializer(
        data={
            "user": {
                "login": user_personal_info_with_image_fixture["user"]["login"],
                "password": user_personal_info_with_image_fixture["user"]["password"],
            },
            "first_name": user_personal_info_with_image_fixture["first_name"],
            "second_name": user_personal_info_with_image_fixture["second_name"],
        }
    )
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert UserPersonalInfo.objects.all().count() == 1
    assert isinstance(instance, UserPersonalInfo)
    assert instance.image is not None


@pytest.mark.django_db
def test_validation_error(user_personal_info_with_image_fixture):
    role_serializer = RoleSerializer(
        data=user_personal_info_with_image_fixture["user"]["role"]
    )
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_personal_info_with_image_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()
    user_personal_info_with_image_fixture["first_name"] = "1"
    user_personal_info_with_image_fixture["second_name"] = "1"

    serializer = UserPersonalInfoSerializer(data=user_personal_info_with_image_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_deserialize(factory_user_personal_info_fixture):
    serializer = UserPersonalInfoSerializer(instance=factory_user_personal_info_fixture)
    assert isinstance(serializer.data, dict)
