import pytest
from faker import Faker
from common.utils.string_utils import generate_valid_login, generate_valid_password
from ..models import (
    Doctor,
    DoctorSummary,
    DoctorSpecialization,
    DoctorDoctorSpecialization,
)
from .factories import (
    DoctorFactory,
    DoctorSummaryFactory,
    DoctorSpecializationFactory,
    DoctorDoctorSpecializationFactory,
)

fake = Faker(locale="ru_RU")

# factories


@pytest.fixture
def factory_doctor_fixture(factory_user_with_role_doctor_fixture) -> Doctor:
    return DoctorFactory.create(user=factory_user_with_role_doctor_fixture)


@pytest.fixture
def factory_doctor_summary_fixture(factory_doctor_fixture) -> DoctorSummary:
    return DoctorSummaryFactory.create(doctor=factory_doctor_fixture)


@pytest.fixture
def factory_doctor_specialization_fixture() -> DoctorSpecialization:
    return DoctorSpecializationFactory.create()


@pytest.fixture
def factory_doctor_doctor_specialization_fixture(
    factory_doctor_specialization_fixture, factory_doctor_fixture
) -> DoctorDoctorSpecialization:
    return DoctorDoctorSpecializationFactory.create(
        doctor=factory_doctor_fixture,
        doctor_specialization=factory_doctor_specialization_fixture,
    )


# dicts


@pytest.fixture
def doctor_specialization_fixture() -> dict:
    return {"name": fake.pystr()}


@pytest.fixture
def doctor_fixture(doctor_role_fixture):
    return {
        "user": {
            "login": generate_valid_login(),
            "password": generate_valid_password(),
            "role": doctor_role_fixture,
        },
    }


@pytest.fixture
def doctor_summary_fixture(doctor_fixture):
    return {
        "doctor": doctor_fixture,
        "short_summary": fake.text(max_nb_chars=1000),
        "summary": fake.text(max_nb_chars=100000),
    }


@pytest.fixture
def doctor_doctor_specializations_fixture(
    doctor_fixture, doctor_specialization_fixture
) -> dict:
    return {
        "doctor": doctor_fixture,
        "doctor_specialization": doctor_specialization_fixture,
    }
