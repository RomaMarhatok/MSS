import pytest
import json
from userApp.models import User
from django.test.client import Client
from rest_framework.authtoken.models import Token
from django.urls import reverse


@pytest.mark.django_db
def test_authentication(factory_user_with_role_patient_fixture, client: Client):
    user: User = factory_user_with_role_patient_fixture
    Token.objects.create(user=user)
    url = reverse("token-user-authentication")
    response = client.post(
        url,
        {"login": user.login, "password": user.password},
    )
    assert response.status_code == 200
    assert "message" in json.loads(response.content.decode("utf-8"))
    assert Token.objects.filter(user__login=user.login).exists()
    assert Token.objects.count() == 1
