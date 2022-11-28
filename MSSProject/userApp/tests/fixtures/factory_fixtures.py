import pytest
from userApp.tests.factories.user_app_factories import (
    RoleFactory,
    UserFactory,
    UserPersonalInfoFactory,
    UserDocumentFactory,
    DoctorTypesFactory,
    DoctorsFactory,
    PatinesFactory,
    ImageForAnalyzesFactory,
    TreatmentsHistoryFactory,
)


@pytest.fixture
def factory_role_fixture():
    return RoleFactory.create()


@pytest.fixture
def factory_user_fixture(factory_role_fixture):
    return UserFactory.create(role=factory_role_fixture)


@pytest.fixture
def factory_user_personal_info_fixture(factory_user_fixture):
    return UserPersonalInfoFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_user_docuemnt_fixture(factory_user_fixture):
    return UserDocumentFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_doctor_type_fixture():
    return DoctorTypesFactory.create()


@pytest.fixture
def factory_doctor_fixture(factory_user_fixture, factory_doctor_type_fixture):
    return DoctorsFactory.create(
        user=factory_user_fixture, doctor_type=factory_doctor_type_fixture
    )


@pytest.fixture
def factory_patient_fixture(factory_user_fixture):
    return PatinesFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_image_for_analyzes_fixture():
    return ImageForAnalyzesFactory.create()


@pytest.fixture
def factory_treatment_history_fixture(
    factory_doctor_fixture, factory_patient_fixture, factory_image_for_analyzes_fixture
):
    return TreatmentsHistoryFactory.create(
        doctor=factory_doctor_fixture,
        patient=factory_patient_fixture,
        image=factory_image_for_analyzes_fixture,
    )
