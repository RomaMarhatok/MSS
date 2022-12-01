import pytest
from userApp.models import ImageForAnalyzes
from userApp.serializers.image_for_analyze_serializer import ImageForAnlyzeSerializer


@pytest.mark.django_db
def test_serialization(image_for_analyzes_with_image_fixture):
    serializer = ImageForAnlyzeSerializer(data=image_for_analyzes_with_image_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert ImageForAnalyzes.objects.all().count() == 1
    assert isinstance(instance, ImageForAnalyzes)


@pytest.mark.django_db
def test_deserialization(factory_image_for_analyzes_fixture):
    serializer = ImageForAnlyzeSerializer(instance=factory_image_for_analyzes_fixture)
    assert isinstance(serializer.data, dict)
