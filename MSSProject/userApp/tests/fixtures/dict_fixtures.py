import pytest
from faker import Faker
from userApp.utils.image_utils import load_image_from_url_to_file
from ...utils.string_utls import generate_valid_password, generate_valid_login

fake = Faker()


@pytest.fixture
def role_fixture() -> dict:
    return {"name": fake.pystr()}


@pytest.fixture
def patient_role_fixture() -> dict:
    return {"name": "patient"}


@pytest.fixture
def user_fixture(role_fixture) -> dict:
    return {
        "login": generate_valid_login(),
        "password": generate_valid_password(),
        "role": role_fixture,
    }


@pytest.fixture
def user_document_type_fixture() -> dict:
    return {
        "name": fake.pystr(),
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
        "gender": fake.simple_profile()["sex"],
        "age": fake.random_number(digits=2),
        "health_status": fake.text(),
    }


@pytest.fixture
def user_personal_info_with_image_fixture(user_personal_info_fixture) -> dict:
    image_url = user_personal_info_fixture["image"]
    gen = load_image_from_url_to_file(image_url)
    img = next(gen)
    user_personal_info_fixture["image"] = img
    yield user_personal_info_fixture
    print(f"Files and folders Was Removed?\nAnswer:{next(gen)}")


@pytest.fixture
def user_location_fixture(user_fixture):
    return {
        "user": user_fixture,
        "country": fake.country(),
        "city": fake.city(),
        "address": fake.address(),
    }


@pytest.fixture
def user_document_fixture(user_fixture, user_document_type_fixture) -> dict:
    return {
        "name": fake.pystr(),
        "content": fake.text(max_nb_chars=10000),
        "user": user_fixture,
        "document_type": user_document_type_fixture,
    }


@pytest.fixture
def doctor_type_fixture() -> dict:
    return {"doctor_type": fake.pystr()}


@pytest.fixture
def doctor_fixture(user_fixture) -> dict:
    return {
        "user": user_fixture,
    }


@pytest.fixture
def patient_fixture(user_fixture) -> dict:
    return {"user": user_fixture}


@pytest.fixture
def image_for_analyzes_fixture() -> dict:
    return {
        "image": fake.image_url(),
        "description": fake.text(max_nb_chars=10000),
    }


@pytest.fixture
def image_for_analyzes_with_image_fixture(image_for_analyzes_fixture) -> dict:
    image_url = image_for_analyzes_fixture["image"]
    gen = load_image_from_url_to_file(image_url)
    img = next(gen)
    image_for_analyzes_fixture["image"] = img
    yield image_for_analyzes_fixture
    print(f"Files and folders Was Removed?\nAnswer:{next(gen)}")


@pytest.fixture
def treatment_history_fixture(doctor_fixture, patient_fixture) -> dict:
    return {
        "description": fake.text(max_nb_chars=10000),
        "doctor": doctor_fixture,
        "patient": patient_fixture,
    }


@pytest.fixture
def doctor_doctor_types_fixture(doctor_fixture, doctor_types_fixture) -> dict:
    return {"doctor": doctor_fixture, "doctor_type": doctor_types_fixture}
