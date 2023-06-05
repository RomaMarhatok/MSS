import pytest
from datetime import datetime
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from appointments.models import Appointments
from user.models import User
from doctor.models import Doctor

client = Client()


@pytest.mark.django_db
def test_patient(factory_appointments_fixture):
    user_slug = factory_appointments_fixture.patient.slug
    doctor_slug = factory_appointments_fixture.doctor.user.slug
    url = reverse("patient-appointments-destroy")
    token = Token.objects.create(user=factory_appointments_fixture.patient).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(
        url,
        {
            "date": factory_appointments_fixture.date,
            "patient_slug": user_slug,
            "doctor_slug": doctor_slug,
        },
        **headers
    )
    assert response.status_code == 200
    assert bool(response.json())
    assert Appointments.objects.count() == 0
    assert User.objects.count() == 2
    assert Doctor.objects.count() == 1


@pytest.mark.django_db
def test_doctor(factory_appointments_fixture):
    user_slug = factory_appointments_fixture.patient.slug
    doctor_slug = factory_appointments_fixture.doctor.user.slug
    url = reverse("doctor-appointments-destroy")
    token = Token.objects.create(user=factory_appointments_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(
        url,
        {
            "date": factory_appointments_fixture.date,
            "patient_slug": user_slug,
            "doctor_slug": doctor_slug,
        },
        **headers
    )
    assert response.status_code == 200
    assert bool(response.json())
    assert Appointments.objects.count() == 0
    assert User.objects.count() == 2
    assert Doctor.objects.count() == 1


@pytest.mark.django_db
def test_user_slug(factory_appointments_fixture):
    doctor_slug = factory_appointments_fixture.doctor.user.slug
    url = reverse("patient-appointments-destroy")
    token = Token.objects.create(user=factory_appointments_fixture.patient).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(
        url,
        {
            "date": factory_appointments_fixture.date,
            "patient_slug": "not-exist",
            "doctor_slug": doctor_slug,
        },
        **headers
    )
    assert response.status_code == 404
    assert bool(response.json())
    assert Appointments.objects.count() == 1
    assert User.objects.count() == 2
    assert Doctor.objects.count() == 1


@pytest.mark.django_db
def test_doctor_slug(factory_appointments_fixture):
    user_slug = factory_appointments_fixture.patient.slug

    url = reverse("patient-appointments-destroy")
    token = Token.objects.create(user=factory_appointments_fixture.patient).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(
        url,
        {
            "date": factory_appointments_fixture.date,
            "patient_slug": user_slug,
            "doctor_slug": "not-exist",
        },
        **headers
    )
    assert response.status_code == 404
    assert bool(response.json())
    assert Appointments.objects.count() == 1
    assert User.objects.count() == 2
    assert Doctor.objects.count() == 1


@pytest.mark.django_db
def test_date(factory_appointments_fixture):
    user_slug = factory_appointments_fixture.patient.slug
    doctor_slug = factory_appointments_fixture.doctor.user.slug

    url = reverse("patient-appointments-destroy")
    token = Token.objects.create(user=factory_appointments_fixture.patient).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(
        url,
        {
            "date": datetime.now(),
            "patient_slug": user_slug,
            "doctor_slug": doctor_slug,
        },
        **headers
    )
    assert response.status_code == 404
    assert bool(response.json())
    assert Appointments.objects.count() == 1
    assert User.objects.count() == 2
    assert Doctor.objects.count() == 1
