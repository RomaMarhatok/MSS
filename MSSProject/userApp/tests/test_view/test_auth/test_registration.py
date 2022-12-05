import pytest
import json
from userApp.models import User, Patient
from django.test.client import Client
from rest_framework.authtoken.models import Token
from django.urls import reverse


@pytest.mark.django_db
def test_registration(factory_patient_role_fixture, user_fixture, client: Client):
    url = reverse("token-user-registration")
    response = client.post(
        url,
        {"login": user_fixture["login"], "password": user_fixture["password"]},
    )
    assert response.status_code == 200
    assert "message" in json.loads(response.content.decode("utf-8"))
    assert Token.objects.filter(user__login=user_fixture["login"]).exists()
    assert Token.objects.count() == 1
    assert User.objects.count() == 1
    assert Patient.objects.count() == 1