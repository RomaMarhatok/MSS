import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from treatment_histories.models import (
    TreatmentHistory,
    ImageForAnalyzes,
    TreatmentHistoryImageForAnalyzes,
)

client = Client()


@pytest.mark.django_db
def test(
    factory_treatment_history_fixture,
    image_for_analyzes_with_image_in_memory,
):
    url = reverse("create-image-for-analyzes")
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    data = {
        "treatment_history_slug": factory_treatment_history_fixture.slug,
        **image_for_analyzes_with_image_in_memory,
    }
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(url, data, **headers, format="multipart")
    assert response.status_code == 200
    assert bool(response.json())
    assert TreatmentHistory.objects.count() == 1
    assert ImageForAnalyzes.objects.count() == 1
    assert TreatmentHistoryImageForAnalyzes.objects.count() == 1
