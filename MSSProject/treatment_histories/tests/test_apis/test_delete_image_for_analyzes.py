import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from treatment_histories.models import (
    TreatmentHistoryImageForAnalyzes,
    ImageForAnalyzes,
    TreatmentHistory,
)
from treatment_histories.serializers import ImageForAnlyzeSerializer

client = Client()


@pytest.mark.django_db
def test(image_for_analyzes_with_image_fixture, factory_treatment_history_fixture):
    serializer = ImageForAnlyzeSerializer(data=image_for_analyzes_with_image_fixture)
    assert serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    TreatmentHistoryImageForAnalyzes.objects.create(
        treatment_history=factory_treatment_history_fixture,
        image_for_analyzes=instance,
    )

    url = reverse("delete-image-for-analyzes")
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    data = {
        "treatment_history_slug": factory_treatment_history_fixture.slug,
        "image_for_analyzes_slug": instance.slug,
    }
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert TreatmentHistoryImageForAnalyzes.objects.count() == 0
    assert ImageForAnalyzes.objects.count() == 0
    assert TreatmentHistory.objects.count() == 1
