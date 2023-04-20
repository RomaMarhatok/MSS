import pytest
from faker import Faker
from common.utils.image_utils import load_image_from_url_to_file, load_image_from_url
from .factories import (
    ImageForAnalyzesFactory,
    TreatmentHistoryFactory,
    TreatmentHistoryImageForAnalyzesFactory,
)
from ..models import (
    ImageForAnalyzes,
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
)

fake = Faker()
# factories


@pytest.fixture
def factory_image_for_analyzes_fixture() -> ImageForAnalyzes:
    return ImageForAnalyzesFactory.create()


@pytest.fixture
def factory_treatment_history_fixture(
    factory_doctor_fixture, factory_user_with_role_patient_fixture
) -> TreatmentHistory:
    return TreatmentHistoryFactory.create(
        doctor=factory_doctor_fixture,
        patient=factory_user_with_role_patient_fixture,
    )


@pytest.fixture
def factory_treatment_history_image_for_analyzes(
    factory_treatment_history_fixture, factory_image_for_analyzes_fixture
) -> TreatmentHistoryImageForAnalyzes:
    return TreatmentHistoryImageForAnalyzesFactory.create(
        treatment_history=factory_treatment_history_fixture,
        image_for_analyzes=factory_image_for_analyzes_fixture,
    )


# dicts


@pytest.fixture
def image_for_analyzes_fixture() -> dict:
    return {
        "image": fake.image_url(),
        "description": fake.text(max_nb_chars=100),
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
def image_for_analyzes_with_image_in_memory(image_for_analyzes_fixture):
    image_url = image_for_analyzes_fixture["image"]
    image_for_analyzes_fixture["image"] = load_image_from_url(image_url)
    return image_for_analyzes_fixture


@pytest.fixture
def treatment_history_fixture(doctor_fixture, patient_fixture) -> dict:
    return {
        "title": fake.text(max_nb_chars=100),
        "short_description": fake.text(max_nb_chars=1000),
        "description": fake.text(max_nb_chars=10000),
        "conclusion": fake.text(max_nb_chars=10000),
        "date": fake.date_time(),
        "doctor": doctor_fixture,
        "patient": patient_fixture,
    }
