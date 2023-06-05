import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(
    factory_treatment_history_fixture, factory_doctor_doctor_specialization_fixture
):
    patient_slug = factory_treatment_history_fixture.patient.slug

    doctor_specialization_slug = (
        factory_doctor_doctor_specialization_fixture.doctor_specialization.slug
    )
    url = reverse(
        "treatment-history-list",
        args=[patient_slug, doctor_specialization_slug],
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
        "treatment-history-list",
        args=["not-exist", "not-exist"],
    )
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.get(url, **headers)
    assert response.status_code == 404
    assert bool(response.json())
