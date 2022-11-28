import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def role_fixture() -> dict:
    return {"name": fake.pystr()}


@pytest.fixture
def user_fixture(role_fixture) -> dict:
    return {
        "login": fake.pystr(),
        "password": fake.password(),
        "role": role_fixture,
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


@pytest.fixture
def user_document_fixture(user_fixture) -> dict:
    return {
        "content": fake.text(),
        "user": user_fixture,
    }


@pytest.fixture
def doctor_types_fixture():
    return {"doctor_type": fake.pystr()}


@pytest.fixture
def doctor_fixture(user_fixture, doctor_types_fixture):
    return {
        "user": user_fixture,
        "doctor_type": [doctor_types_fixture, {"doctor_type": fake.pystr()}],
    }


@pytest.fixture
def patient_fixture(user_fixture):
    return {"user": user_fixture}


@pytest.fixture
def image_for_analyzes_fixture():
    return {
        "image": fake.image_url(),
        "description": fake.text(),
    }


@pytest.fixture
def treatment_history_fixture(
    doctor_fixture, patient_fixture, image_for_analyzes_fixture
):
    return {
        "description": fake.text(),
        "doctor": doctor_fixture,
        "patient": patient_fixture,
        "image": image_for_analyzes_fixture,
    }
