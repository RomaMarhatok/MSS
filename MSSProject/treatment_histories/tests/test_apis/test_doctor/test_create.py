import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from treatment_histories.models import TreatmentHistory

client = Client()


@pytest.mark.django_db
def test(
    factory_doctor_fixture,
    factory_user_with_role_patient_fixture,
    treatment_history_fixture,
):
    url = reverse("treatment-history-create")
    token = Token.objects.create(user=factory_doctor_fixture.user).key
    treatment_history_fixture[
        "patient_slug"
    ] = factory_user_with_role_patient_fixture.slug
    treatment_history_fixture["doctor_slug"] = factory_doctor_fixture.user.slug

    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    response = client.post(url, treatment_history_fixture, **headers)
    assert response.status_code == 200
    assert TreatmentHistory.objects.count() == 1
