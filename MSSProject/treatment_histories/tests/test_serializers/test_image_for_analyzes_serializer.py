import pytest
from treatment_histories.models import ImageForAnalyzes
from treatment_histories.serializers import (
    ImageForAnlyzeSerializer,
)
from rest_framework.exceptions import ValidationError


@pytest.mark.django_db
def test_serialization(image_for_analyzes_with_image_fixture):
    serializer = ImageForAnlyzeSerializer(data=image_for_analyzes_with_image_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert ImageForAnalyzes.objects.count() == 1
    assert isinstance(instance, ImageForAnalyzes)
    assert instance.image is not None


@pytest.mark.django_db
def test_dublicates(image_for_analyzes_with_image_in_memory):
    serializer = ImageForAnlyzeSerializer(data=image_for_analyzes_with_image_in_memory)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    assert ImageForAnalyzes.objects.count() == 1
    assert isinstance(instance, ImageForAnalyzes)
    assert instance.image is not None
    with pytest.raises(ValidationError):
        serializer = ImageForAnlyzeSerializer(
            data=image_for_analyzes_with_image_in_memory
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()


@pytest.mark.django_db
def test_deserialization(factory_image_for_analyzes_fixture):
    serializer = ImageForAnlyzeSerializer(instance=factory_image_for_analyzes_fixture)
    assert isinstance(serializer.data, dict)
