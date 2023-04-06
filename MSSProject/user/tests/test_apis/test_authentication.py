import pytest
from user.models import Role
from django.urls import reverse
from django.test.client import Client

client = Client()


@pytest.mark.django_db
def test(user_personal_info_with_image_fixture, user_location_fixture, patient_fixture):
    Role.objects.create(name=Role.PATIENT)
    data = {
        **user_personal_info_with_image_fixture,
        **user_location_fixture,
        **patient_fixture,
    }
    url = reverse("user-registration")
    response = client.post(url, data)
    assert response.status_code == 200

    authentication_data = {
        "login": data.get("login", None),
        "password": data.get("password", None),
    }
    url = reverse("user-authentication")
    response = client.post(url, authentication_data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_bad(
    user_personal_info_with_image_fixture, user_location_fixture, patient_fixture
):
    Role.objects.create(name=Role.PATIENT)
    data = {
        **user_personal_info_with_image_fixture,
        **user_location_fixture,
        **patient_fixture,
    }
    url = reverse("user-registration")
    response = client.post(url, data)
    assert response.status_code == 200

    authentication_data = {
        "login": data.get("login", None),
        "password": "",
    }
    url = reverse("user-authentication")
    response = client.post(url, authentication_data)
    assert response.status_code == 400
