import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_doctor_fixture):
    url = reverse("doctors-list")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())
