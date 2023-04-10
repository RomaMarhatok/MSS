import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token


client = Client()


@pytest.mark.django_db
def test(factory_treatment_history_fixture):
    patient_slug = factory_treatment_history_fixture.patient.slug
    url = reverse(
        "patient-treatment-history-list",
        args=[patient_slug],
    )
    token = Token.objects.create(user=factory_treatment_history_fixture.patient).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())
