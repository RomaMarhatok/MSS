import pytest
from django.urls import reverse
from django.test.client import Client
from rest_framework.authtoken.models import Token
from treatment_histories.serializers import TreatmentHistorySerializer
from treatment_histories.models import TreatmentHistory
from faker import Faker

fake = Faker()
client = Client()


@pytest.mark.django_db
def test(factory_treatment_history_fixture):
    url = reverse("update-treatment-history")
    token = Token.objects.create(user=factory_treatment_history_fixture.doctor.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    ts_dict = TreatmentHistorySerializer(
        instance=factory_treatment_history_fixture
    ).data
    ts_dict["treatment_history_slug"] = factory_treatment_history_fixture.slug
    data = ts_dict
    conclusion = "test"
    data["conclusion"] = conclusion
    assert factory_treatment_history_fixture.conclusion != conclusion
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    assert TreatmentHistory.objects.count() == 1
    ts = TreatmentHistory.objects.first()
    assert ts.conclusion == conclusion
    assert ts.slug == factory_treatment_history_fixture.slug
