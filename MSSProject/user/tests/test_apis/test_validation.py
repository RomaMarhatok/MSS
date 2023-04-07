import pytest
from django.test.client import Client
from django.urls import reverse
from common.utils.string_utils import generate_valid_login, generate_valid_password

client = Client()


@pytest.mark.django_db
def test_user(factory_user_with_role_patient_fixture):
    url = reverse("validate-user")
    data = {
        "login": generate_valid_login(),
        "password": generate_valid_password(),
    }
    response = client.post(url, data=data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_bad(factory_user_with_role_patient_fixture):
    url = reverse("validate-user")
    data = {
        "login": factory_user_with_role_patient_fixture.login,
        "password": factory_user_with_role_patient_fixture.password,
    }
    response = client.post(url, data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_personal_info(
    user_personal_info_with_image_fixture, user_personal_info_fixture
):
    url = reverse("validate-info")
    response = client.post(url, data=user_personal_info_fixture)
    assert response.status_code == 200


@pytest.mark.django_db
def test_personal_info_bad(factory_user_personal_info_fixture):
    url = reverse("validate-info")
    data = {
        "first_name": factory_user_personal_info_fixture.first_name,
        "second_name": factory_user_personal_info_fixture.second_name,
        "patronymic": factory_user_personal_info_fixture.patronymic,
        "email": factory_user_personal_info_fixture.email,
        "gender": factory_user_personal_info_fixture.gender,
        "age": factory_user_personal_info_fixture.age,
    }
    response = client.post(url, data=data)
    assert response.status_code == 400
