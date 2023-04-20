import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from physical.models import PhysicalParameters

client = Client()


@pytest.mark.django_db
def test(
    factory_physical_parameters_fixture,
    physical_parameters_fixture,
    factory_doctor_fixture,
):
    url = reverse("physical-create")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "user_slug": factory_physical_parameters_fixture.user.slug,
        **physical_parameters_fixture,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    # 2 because factory_physical_parameters_fixture also create instance
    assert PhysicalParameters.objects.count() == 2


@pytest.mark.django_db
def test_bad(
    physical_parameters_fixture,
    factory_doctor_fixture,
):
    url = reverse("physical-create")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "user_slug": "not-exist",
        **physical_parameters_fixture,
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 400
    assert bool(response.json())
    assert PhysicalParameters.objects.count() == 0
