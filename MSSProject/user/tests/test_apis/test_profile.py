import pytest
from django.urls import reverse
from django.test.client import Client
from user.models import Role, User
from rest_framework.authtoken.models import Token

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
    slug = User.objects.first().slug
    token = Token.objects.first().key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    url = reverse("user-profile", args=[slug])
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert bool(response.json())
