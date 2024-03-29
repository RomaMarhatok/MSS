import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_treatment_history_fixture):

    url = reverse(
        "treatment-history-retrieve",
        args=[factory_treatment_history_fixture.slug],
    )
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())


@pytest.mark.django_db
def test_bad(factory_treatment_history_fixture):
    url = reverse(
        "treatment-history-retrieve",
        args=["not-exist"],
    )
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 404
    assert bool(response.json())
