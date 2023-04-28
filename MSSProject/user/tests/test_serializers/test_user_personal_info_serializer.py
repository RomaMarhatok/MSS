import pytest
from django.test.client import RequestFactory
from rest_framework.validators import ValidationError
from user.models import UserPersonalInfo
from user.serializers.role_serializer import RoleSerializer
from user.serializers.user_personal_info_serializer import UserPersonalInfoSerializer
from user.serializers.user_serializer import UserSerializer


@pytest.mark.django_db
def test_serialization(user_personal_info_fixture):
    role_serializer = RoleSerializer(data=user_personal_info_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_personal_info_fixture["user"])
    assert user_serializer.is_valid()
    user = user_serializer.save()
    user_personal_info_fixture.update({"user_slug": user.slug})
    request = RequestFactory().request()
    serializer = UserPersonalInfoSerializer(
        data=user_personal_info_fixture, context={"request": request}
    )
    assert serializer.is_valid(raise_exception=True)
    instance: UserPersonalInfo = serializer.save()
    assert UserPersonalInfo.objects.all().count() == 1
    assert isinstance(instance, UserPersonalInfo)


@pytest.mark.django_db
def test_serialize_without_fields(user_personal_info_fixture):
    role_serializer = RoleSerializer(data=user_personal_info_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_personal_info_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()
    serializer = UserPersonalInfoSerializer(
        data={
            "user": {
                "login": user_personal_info_fixture["user"]["login"],
                "password": user_personal_info_fixture["user"]["password"],
            },
            "first_name": user_personal_info_fixture["first_name"],
            "second_name": user_personal_info_fixture["second_name"],
        }
    )
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_validation_error(user_personal_info_fixture):
    role_serializer = RoleSerializer(data=user_personal_info_fixture["user"]["role"])
    assert role_serializer.is_valid()
    role_serializer.save()

    user_serializer = UserSerializer(data=user_personal_info_fixture["user"])
    assert user_serializer.is_valid()
    user_serializer.save()
    user_personal_info_fixture["first_name"] = "1"
    user_personal_info_fixture["second_name"] = "1"

    serializer = UserPersonalInfoSerializer(data=user_personal_info_fixture)
    with pytest.raises(ValidationError):
        assert serializer.is_valid(raise_exception=True)


@pytest.mark.django_db
def test_serialization_with_absolute_image_url(factory_user_personal_info_fixture):
    request = RequestFactory().request()
    serializer = UserPersonalInfoSerializer(
        instance=factory_user_personal_info_fixture, context={"request": request}
    )
    assert isinstance(serializer.data, dict)


@pytest.mark.django_db
def test_serialization_update(factory_user_personal_info_fixture):
    assert factory_user_personal_info_fixture.health_status != "test"
    serialized_instance = UserPersonalInfoSerializer(
        instance=factory_user_personal_info_fixture
    ).data
    serialized_instance["health_status"] = "test"
    serializer = UserPersonalInfoSerializer(
        instance=factory_user_personal_info_fixture,
        data=serialized_instance,
        partial=True,
    )
    assert serializer.is_valid(raise_exception=True)
    serializer.save()
    instance = UserPersonalInfo.objects.get(
        user__slug=factory_user_personal_info_fixture.user.slug
    )
    assert instance.health_status == "test"


@pytest.mark.django_db
def test_deserialization(factory_user_personal_info_fixture):
    serializer = UserPersonalInfoSerializer(instance=factory_user_personal_info_fixture)
    assert isinstance(serializer.data, dict)
