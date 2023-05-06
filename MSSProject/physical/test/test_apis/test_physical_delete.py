import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from physical.models import PhysicalParameters

client = Client()


@pytest.mark.django_db
def test(factory_physical_parameters_fixture, factory_doctor_fixture):
    url = reverse("physical-delete")
    slug = PhysicalParameters.objects.first().slug
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {"slug": slug}
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert PhysicalParameters.objects.count() == 0


@pytest.mark.django_db
def test_bad(factory_physical_parameters_fixture, factory_doctor_fixture):
    url = reverse("physical-delete")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {"slug": "not-exist"}
    response = client.post(url, data, **headers)
    assert response.status_code == 404
    assert bool(response.json())
    assert PhysicalParameters.objects.count() == 1
