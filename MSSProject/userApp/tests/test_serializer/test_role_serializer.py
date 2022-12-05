import pytest
from userApp.serializers.role_serializer import RoleSerializer
from userApp.models import Role


@pytest.mark.django_db
def test_serialization(role_fixture):
    serializer = RoleSerializer(data=role_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()

    assert Role.objects.all().count() == 1
    assert isinstance(instance, Role)
    assert hasattr(instance, "slug")
    assert instance.slug != "default"
    assert instance.slug != ""


@pytest.mark.django_db
def test_deserialization(factory_role_fixture):
    serializer = RoleSerializer(instance=factory_role_fixture)
    assert isinstance(serializer.data, dict)
    assert "slug" in serializer.data
    assert serializer.data["slug"] != "default"
    assert serializer.data["slug"] != ""
