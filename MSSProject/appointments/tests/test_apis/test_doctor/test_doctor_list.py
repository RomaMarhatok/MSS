import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_appointments_fixture):
    doctor_slug = factory_appointments_fixture.doctor.user.slug
    url = reverse("doctor-appoitments-list", args=[doctor_slug])
    token = Token.objects.create(user=factory_appointments_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())


@pytest.mark.django_db
def test_bad(factory_appointments_fixture):
    url = reverse("doctor-appoitments-list", args=["not-exist"])
    token = Token.objects.create(user=factory_appointments_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 404
    assert bool(response.json())
