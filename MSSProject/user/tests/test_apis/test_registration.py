import pytest
from django.test.client import Client
from django.urls import reverse
from user.models import Role, User, UserLocation, UserPersonalInfo

client = Client()


@pytest.mark.django_db
def test():
    Role.objects.create(name=Role.PATIENT)
    data = {
        "address": "adress",
        "age": 12,
        "city": "г.Минск",
        "country": "Belarus",
        "email": "r.marhatok@yandex.by",
        "first_name": "Roma",
        "gender": "M",
        "login": "testlogin",
        "password": "testpassword",
        "patronymic": "Roma",
        "second_name": "Roma",
        "email_message": "test",
    }

    url = reverse("user-registration")
    response = client.post(url, data)
    assert response.status_code == 200
    assert User.objects.count() == 1
    assert UserLocation.objects.count() == 1
    assert UserPersonalInfo.objects.count() == 1
    assert not User.objects.last().verified


@pytest.mark.django_db
def test_bad():
    Role.objects.create(name=Role.PATIENT)
    data = {
        "address": "adress",
        "age": 12,
        "country": "",
        "city": "г.Минск",
        "email": "r.marhatok@yandex.by",
        "first_name": "Roma",
        "gender": "M",
        "login": "sadadad",
        "password": "asdasdmsadsa",
        "patronymic": "Roma",
        "second_name": "Roma",
        "email_message": "test",
    }
    url = reverse("user-registration")
    response = client.post(url, data)
    assert response.status_code == 400
    assert User.objects.count() == 0
    assert UserLocation.objects.count() == 0
    assert UserPersonalInfo.objects.count() == 0


# @pytest.mark.django_db
# def test_not_exist_mail(
#     user_personal_info_fixture, user_location_fixture, patient_fixture
# ):
#     Role.objects.create(name=Role.PATIENT)
#     data = {
#         **user_personal_info_fixture,
#         **user_location_fixture,
#         **patient_fixture,
#         "email_message": "test",
#     }
#     url = reverse("user-registration")
#     response = client.post(url, data)
#     assert response.status_code == 400
#     assert User.objects.count() == 0
#     assert UserLocation.objects.count() == 0
#     assert UserPersonalInfo.objects.count() == 0
