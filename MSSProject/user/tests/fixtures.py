import pytest
from common.utils.image_utils import load_image_from_url_to_file
from common.utils.string_utils import generate_valid_login, generate_valid_password
from faker import Faker

from ..models import Role, User, UserLocation, UserPersonalInfo
from .factories import (
    RoleFactory,
    UserFactory,
    UserLocationFactory,
    UserPersonalInfoFactory,
)

fake = Faker()

# factories


@pytest.fixture
def factory_patient_role_fixture() -> Role:
    return RoleFactory.create(name=Role.PATIENT)


@pytest.fixture
def factory_doctor_role_fixture() -> Role:
    return RoleFactory.create(name=Role.DOCTOR)


@pytest.fixture
def factory_user_with_role_patient_fixture(factory_patient_role_fixture) -> User:
    return UserFactory.create(
        login=generate_valid_login(), role=factory_patient_role_fixture
    )


@pytest.fixture
def factory_user_with_role_doctor_fixture(factory_doctor_role_fixture) -> User:
    return UserFactory.create(
        login=generate_valid_login(), role=factory_doctor_role_fixture
    )


@pytest.fixture
def factory_user_personal_info_fixture(
    factory_user_with_role_patient_fixture,
) -> UserPersonalInfo:
    return UserPersonalInfoFactory.create(user=factory_user_with_role_patient_fixture)


@pytest.fixture
def factory_user_location_fixture(
    factory_user_with_role_patient_fixture,
) -> UserLocation:
    return UserLocationFactory.create(user=factory_user_with_role_patient_fixture)


# dicts
@pytest.fixture
def patient_role_fixture() -> dict:
    return {"name": Role.PATIENT}


@pytest.fixture
def doctor_role_fixture() -> dict:
    return {"name": Role.DOCTOR}


@pytest.fixture
def patient_fixture(patient_role_fixture) -> dict:
    return {
        "login": generate_valid_login(),
        "password": generate_valid_password(),
        "role": patient_role_fixture,
    }


@pytest.fixture
def user_personal_info_fixture(patient_fixture) -> dict:
    return {
        "user": patient_fixture,
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
def user_location_fixture(patient_fixture):
    return {
        "user": patient_fixture,
        "country": fake.country(),
        "city": fake.city(),
        "address": fake.address(),
    }
