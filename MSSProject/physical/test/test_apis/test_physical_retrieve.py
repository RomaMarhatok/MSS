import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from physical.models import PhysicalParameters

client = Client()


@pytest.mark.django_db
def test(factory_physical_parameters_fixture, factory_doctor_fixture):
    url = reverse("physical-retrieve", args=[PhysicalParameters.objects.first().slug])
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())


@pytest.mark.django_db
def test_bad(factory_physical_parameters_fixture, factory_doctor_fixture):
    url = reverse("physical-retrieve", args=["not-exist"])
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 404
    assert bool(response.json())
