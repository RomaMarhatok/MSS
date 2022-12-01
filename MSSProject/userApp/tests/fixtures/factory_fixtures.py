import pytest
from userApp.tests.factories.user_app_factories import (
    RoleFactory,
    UserFactory,
    UserPersonalInfoFactory,
    UserDocumentFactory,
    DoctorTypesFactory,
    DoctorFactory,
    PatinesFactory,
    ImageForAnalyzesFactory,
    TreatmentsHistoryFactory,
    DoctorDoctorTypesFactory,
    TreatmentHistoryImageForAnalyzesFactory,
)
from ...models import (
    Role,
    User,
    UserDocument,
    UserPersonalInfo,
    Patient,
    Doctor,
    DoctorDoctorTypes,
    DoctorType,
    ImageForAnalyzes,
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
)


@pytest.fixture
def factory_role_fixture() -> Role:
    return RoleFactory.create()


@pytest.fixture
def factory_user_fixture(factory_role_fixture) -> User:
    return UserFactory.create(role=factory_role_fixture)


@pytest.fixture
def factory_user_personal_info_fixture(factory_user_fixture) -> UserPersonalInfo:
    return UserPersonalInfoFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_user_docuemnt_fixture(factory_user_fixture) -> UserDocument:
    return UserDocumentFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_doctor_type_fixture() -> DoctorType:
    return DoctorTypesFactory.create()


@pytest.fixture
def factory_doctor_fixture(factory_user_fixture) -> Doctor:
    return DoctorFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_doctor_doctor_types_fixture(
    factory_doctor_type_fixture, factory_doctor_fixture
) -> DoctorDoctorTypes:
    return DoctorDoctorTypesFactory.create(
        doctor=factory_doctor_fixture, doctor_type=factory_doctor_type_fixture
    )


@pytest.fixture
def factory_patient_fixture(factory_user_fixture) -> Patient:
    return PatinesFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_image_for_analyzes_fixture() -> ImageForAnalyzes:
    return ImageForAnalyzesFactory.create()


@pytest.fixture
def factory_treatment_history_fixture(
    factory_doctor_fixture, factory_patient_fixture
) -> TreatmentHistory:
    return TreatmentsHistoryFactory.create(
        doctor=factory_doctor_fixture,
        patient=factory_patient_fixture,
    )


@pytest.fixture
def factory_treatment_history_image_for_analyzes(
    factory_treatment_history_fixture, factory_image_for_analyzes_fixture
) -> TreatmentHistoryImageForAnalyzes:
    return TreatmentHistoryImageForAnalyzesFactory.create(
        treatment_history=factory_treatment_history_fixture,
        image_for_analyzes=factory_image_for_analyzes_fixture,
    )
