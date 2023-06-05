import pytest
from django.urls import reverse
from django.test.client import Client
from user.models import Role, User, UserPersonalInfo
from user.serializers import UserPersonalInfoSerializer
from rest_framework.authtoken.models import Token

client = Client()


@pytest.mark.django_db
def test(factory_user_personal_info_fixture):
    serializer = UserPersonalInfoSerializer(instance=factory_user_personal_info_fixture)
    token = Token.objects.create(user=factory_user_personal_info_fixture.user).key
    headers = {
        "HTTP_AUTHORIZATION": "Bearer " + token,
    }
    data = serializer.data
    data["health_status"] = "test"
    url = reverse("update-user-profile")
    response = client.post(url, data, **headers)
    assert response.status_code == 200
    assert bool(response.json())
    personal_info = UserPersonalInfo.objects.first()
    assert personal_info.health_status == "test"
