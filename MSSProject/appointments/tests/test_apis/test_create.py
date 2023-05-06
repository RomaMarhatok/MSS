import pytest
from datetime import datetime, timedelta
from django.test.client import Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from appointments.models import Appointments

client = Client()


@pytest.mark.django_db
def test_patient(
    factory_user_with_role_patient_fixture,
    factory_doctor_doctor_specialization_fixture,
):
    url = reverse("patient-appointments-create")
    token = Token.objects.create(user=factory_user_with_role_patient_fixture).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "doctor_slug": factory_doctor_doctor_specialization_fixture.doctor.user.slug,
        "patient_slug": factory_user_with_role_patient_fixture.slug,
        "doctor_specialization_slug": factory_doctor_doctor_specialization_fixture.doctor_specialization.slug,
        "date": datetime.now(),
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert Appointments.objects.count() == 1


@pytest.mark.django_db
def test_doctor(
    factory_user_with_role_patient_fixture,
    factory_doctor_doctor_specialization_fixture,
):
    url = reverse("patient-appointments-create")
    token = Token.objects.create(
        user=factory_doctor_doctor_specialization_fixture.doctor.user
    ).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "doctor_slug": factory_doctor_doctor_specialization_fixture.doctor.user.slug,
        "patient_slug": factory_user_with_role_patient_fixture.slug,
        "doctor_specialization_slug": factory_doctor_doctor_specialization_fixture.doctor_specialization.slug,
        "date": datetime.now(),
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert Appointments.objects.count() == 1


@pytest.mark.django_db
def test_doctor_slug(
    factory_user_with_role_patient_fixture,
    factory_doctor_doctor_specialization_fixture,
):
    url = reverse("patient-appointments-create")
    token = Token.objects.create(user=factory_user_with_role_patient_fixture).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "doctor_slug": "not-exist",
        "patient_slug": factory_user_with_role_patient_fixture.slug,
        "doctor_specialization_slug": factory_doctor_doctor_specialization_fixture.doctor_specialization.slug,
        "date": datetime.now(),
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 404
    assert bool(response.json())
    assert Appointments.objects.count() == 0


@pytest.mark.django_db
def test_patient_slug(
    factory_user_with_role_patient_fixture,
    factory_doctor_doctor_specialization_fixture,
):
    url = reverse("patient-appointments-create")
    token = Token.objects.create(user=factory_user_with_role_patient_fixture).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "doctor_slug": factory_doctor_doctor_specialization_fixture.doctor.user.slug,
        "patient_slug": "not-exist",
        "doctor_specialization_slug": factory_doctor_doctor_specialization_fixture.doctor_specialization.slug,
        "date": datetime.now(),
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 404
    assert bool(response.json())
    assert Appointments.objects.count() == 0


@pytest.mark.django_db
def test_past_time(
    factory_user_with_role_patient_fixture,
    factory_doctor_doctor_specialization_fixture,
):
    url = reverse("patient-appointments-create")
    token = Token.objects.create(user=factory_user_with_role_patient_fixture).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "doctor_slug": factory_doctor_doctor_specialization_fixture.doctor.user.slug,
        "patient_slug": factory_user_with_role_patient_fixture.slug,
        "doctor_specialization_slug": factory_doctor_doctor_specialization_fixture.doctor_specialization.slug,
        "date": datetime.now() - timedelta(days=10),
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 400
    assert bool(response.json())
    assert Appointments.objects.count() == 0


@pytest.mark.django_db
def test_future_time(
    factory_user_with_role_patient_fixture,
    factory_doctor_doctor_specialization_fixture,
):
    url = reverse("patient-appointments-create")
    token = Token.objects.create(user=factory_user_with_role_patient_fixture).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = {
        "doctor_slug": factory_doctor_doctor_specialization_fixture.doctor.user.slug,
        "patient_slug": factory_user_with_role_patient_fixture.slug,
        "doctor_specialization_slug": factory_doctor_doctor_specialization_fixture.doctor_specialization.slug,
        "date": datetime.now() + timedelta(days=10),
    }
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert Appointments.objects.count() == 1
