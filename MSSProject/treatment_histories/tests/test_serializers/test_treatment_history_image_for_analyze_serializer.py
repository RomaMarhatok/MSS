import pytest
from treatment_histories.serializers.treatment_history_image_for_analyze_serializer import (
    TreatmentHistoryImageForAnalyzesSerializer,
)

from treatment_histories.models import TreatmentHistoryImageForAnalyzes


@pytest.mark.django_db
def test_serializer(
    factory_treatment_history_fixture, factory_image_for_analyzes_fixture
):
    serializer = TreatmentHistoryImageForAnalyzesSerializer(
        data={
            "treatment_history": factory_treatment_history_fixture.pk,
            "image_for_analyzes": factory_image_for_analyzes_fixture.pk,
        }
    )
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()

    assert TreatmentHistoryImageForAnalyzes.objects.all().count() == 1
    assert isinstance(instance, TreatmentHistoryImageForAnalyzes)


@pytest.mark.django_db
def test_deserializer(factory_treatment_history_image_for_analyzes):
    serializer = TreatmentHistoryImageForAnalyzesSerializer(
        instance=factory_treatment_history_image_for_analyzes
    )
    assert isinstance(serializer.data, dict)
