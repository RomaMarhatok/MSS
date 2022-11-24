import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def role_fixture() -> dict:
    return {"name": fake.pystr()}


@pytest.fixture
def user_fixture(role_fixture) -> dict:
    return {
        "username": fake.profile()["username"],
        "login": fake.pystr(),
        "password": fake.password(),
        "role": role_fixture,
    }


@pytest.fixture
def document_type_fixture() -> dict:
    return {"document_type": fake.pystr()}


@pytest.fixture
def user_document_fixture(document_type_fixture, user_fixture) -> dict:
    return {
        "content": fake.pystr(),
        "doctype": document_type_fixture,
        "user": user_fixture,
    }


@pytest.fixture
def user_personal_info_fixture(user_fixture) -> dict:
    return {
        "user": user_fixture,
        "image": fake.image_url(),
        "first_name": fake.first_name(),
        "second_name": fake.last_name(),
        "patronymic": fake.last_name(),
        "email": fake.email(),
    }
