import pytest
from userApp.tests.factories.user_app_factories import (
    RoleFactory,
    UserFactory,
    UserPersonalInfoFactory,
    DocumentFactory,
    DoctorSpecializationFactory,
    DoctorFactory,
    PatientFactory,
    ImageForAnalyzesFactory,
    TreatmentHistoryFactory,
    DoctorDoctorSpecializationFactory,
    TreatmentHistoryImageForAnalyzesFactory,
    DocumentTypeFactory,
    UserLocationFactory,
    DocumentCreatorFactory,
    DoctorSummaryFactory,
    AppointmentsFactory,
)
from ...models import (
    Role,
    User,
    Document,
    UserPersonalInfo,
    Patient,
    Doctor,
    DoctorDoctorSpecialization,
    DoctorSpecialization,
    ImageForAnalyzes,
    DocumentType,
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
    UserLocation,
    DocumentCreator,
    DoctorSummary,
    Appointments,
)


@pytest.fixture
def factory_role_fixture() -> Role:
    return RoleFactory.create()


@pytest.fixture
def factory_patient_role_fixture() -> Role:
    return RoleFactory.create(name="patient")


@pytest.fixture
def factory_user_fixture(factory_role_fixture) -> User:
    return UserFactory.create(role=factory_role_fixture)


@pytest.fixture
def factory_user_with_role_patient_fixture(factory_patient_role_fixture) -> User:
    return UserFactory.create(role=factory_patient_role_fixture)


@pytest.fixture
def factory_user_personal_info_fixture(factory_user_fixture) -> UserPersonalInfo:
    return UserPersonalInfoFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_user_location_fixture(factory_user_fixture) -> UserLocation:
    return UserLocationFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_document_fixture(
    factory_user_fixture, factory_document_type_fixture
) -> Document:
    return DocumentFactory.create(
        user=factory_user_fixture, document_type=factory_document_type_fixture
    )


@pytest.fixture
def factory_doctor_specialization_fixture() -> DoctorSpecialization:
    return DoctorSpecializationFactory.create()


@pytest.fixture
def factory_document_type_fixture() -> DocumentType:
    return DocumentTypeFactory.create()


@pytest.fixture
def factory_doctor_fixture(factory_user_fixture) -> Doctor:
    return DoctorFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_doctor_doctor_specialization_fixture(
    factory_doctor_specialization_fixture, factory_doctor_fixture
) -> DoctorDoctorSpecialization:
    return DoctorDoctorSpecializationFactory.create(
        doctor=factory_doctor_fixture,
        doctor_specialization=factory_doctor_specialization_fixture,
    )


@pytest.fixture
def factory_patient_fixture(factory_user_fixture) -> Patient:
    return PatientFactory.create(user=factory_user_fixture)


@pytest.fixture
def factory_image_for_analyzes_fixture() -> ImageForAnalyzes:
    return ImageForAnalyzesFactory.create()


@pytest.fixture
def factory_treatment_history_fixture(
    factory_doctor_fixture, factory_patient_fixture
) -> TreatmentHistory:
    return TreatmentHistoryFactory.create(
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


@pytest.fixture
def factory_document_creator_fixture(
    factory_document_fixture, factory_doctor_fixture
) -> DocumentCreator:
    return DocumentCreatorFactory.create(
        document=factory_document_fixture, creator=factory_doctor_fixture
    )


@pytest.fixture
def factory_document_summary_fixture(factory_doctor_fixture) -> DoctorSummary:
    return DoctorSummaryFactory.create(doctor=factory_doctor_fixture)


@pytest.fixture
def factory_appointments_fixture(
    factory_doctor_fixture, factory_patient_fixture
) -> Appointments:
    return AppointmentsFactory.create(
        doctor=factory_doctor_fixture, patient=factory_patient_fixture
    )
