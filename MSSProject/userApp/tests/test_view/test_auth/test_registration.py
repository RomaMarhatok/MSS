import pytest
import json
from userApp.models import User, Patient, UserPersonalInfo
from django.test.client import Client
from django.urls import reverse


@pytest.mark.django_db
def test_registration(
    factory_patient_role_fixture,
    user_personal_info_fixture,
    user_fixture,
    client: Client,
):
    url = reverse("token-user-registration")
    response = client.post(
        url,
        {
            "login": user_fixture["login"],
            "password": user_fixture["password"],
            "first_name": user_personal_info_fixture["first_name"],
            "second_name": user_personal_info_fixture["second_name"],
        },
    )
    assert response.status_code == 200
    assert "message" in json.loads(response.content.decode("utf-8"))
    assert User.objects.count() == 1
    assert Patient.objects.count() == 1
    assert UserPersonalInfo.objects.count() == 1
