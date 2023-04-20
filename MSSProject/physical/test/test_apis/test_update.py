import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from physical.models import PhysicalParameters

client = Client()


@pytest.mark.django_db
def test(
    factory_physical_parameters_fixture,
    factory_doctor_fixture,
):
    url = reverse("physical-update")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "user_slug": factory_physical_parameters_fixture.user.slug,
        "slug": factory_physical_parameters_fixture.slug,
        "height": 12.0,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert PhysicalParameters.objects.count() == 1
    assert PhysicalParameters.objects.first().height == 12.0


@pytest.mark.django_db
def test_bad(
    factory_physical_parameters_fixture,
    factory_doctor_fixture,
):
    url = reverse("physical-update")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }

    data = {
        "user_slug": factory_physical_parameters_fixture.user.slug,
        "slug": "not-exist",
        "height": 12.0,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 404
    assert bool(response.json())
    assert PhysicalParameters.objects.count() == 1
    assert PhysicalParameters.objects.first().height != 12.0
