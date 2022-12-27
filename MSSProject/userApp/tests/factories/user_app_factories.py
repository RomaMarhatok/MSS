from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from ...utils.string_utls import generate_valid_password, generate_valid_login
from ...utils.image_utils import load_image_from_url
from ...models import (
    Doctor,
    DoctorSpecialization,
    ImageForAnalyzes,
    Patient,
    Role,
    TreatmentHistory,
    User,
    Document,
    DocumentType,
    UserPersonalInfo,
    DoctorDoctorSpecialization,
    TreatmentHistoryImageForAnalyzes,
    UserLocation,
    DocumentCreator,
    DoctorSummary,
)

fake = Faker()


class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Role
        django_get_or_create = ("name",)

    name = fake.pystr()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    login = generate_valid_login()
    password = generate_valid_password()
    role = SubFactory(RoleFactory)


class DocumentTypeFactory(DjangoModelFactory):
    class Meta:
        model = DocumentType

    name = fake.pystr()


class UserPersonalInfoFactory(DjangoModelFactory):
    class Meta:
        model = UserPersonalInfo

    user = SubFactory(UserFactory)
    image = load_image_from_url(fake.image_url())
    first_name = fake.first_name()
    second_name = fake.last_name()
    patronymic = fake.last_name()
    email = fake.email()
    gender = fake.simple_profile()["sex"]
    age = fake.random_number(digits=2)
    health_status = fake.text(max_nb_chars=10000)


class DocumentFactory(DjangoModelFactory):
    class Meta:
        model = Document

    content = fake.text(max_nb_chars=10000)
    name = fake.pystr()
    user = SubFactory(UserFactory)
    document_type = SubFactory(DocumentTypeFactory)


class UserLocationFactory(DjangoModelFactory):
    class Meta:
        model = UserLocation

    user = SubFactory(User)
    country = fake.country()
    city = fake.city()
    address = fake.address()


class DoctorSpecializationFactory(DjangoModelFactory):
    class Meta:
        model = DoctorSpecialization

    name = fake.pystr()


class DoctorFactory(DjangoModelFactory):
    class Meta:
        model = Doctor

    user = SubFactory(UserFactory)


class DoctorDoctorSpecializationFactory(DjangoModelFactory):
    class Meta:
        model = DoctorDoctorSpecialization

    doctor = SubFactory(DoctorFactory)
    doctor_specialization = SubFactory(DoctorSpecializationFactory)


class PatientFactory(DjangoModelFactory):
    class Meta:
        model = Patient

    user = SubFactory(UserFactory)


class ImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = ImageForAnalyzes

    image = load_image_from_url(fake.image_url())
    description = fake.text(max_nb_chars=10000)


class TreatmentHistoryFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistory

    description = fake.text(max_nb_chars=10000)
    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(PatientFactory)


class TreatmentHistoryImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistoryImageForAnalyzes

    treatment_history = SubFactory(TreatmentHistoryFactory)
    image_for_analyzes = SubFactory(ImageForAnalyzesFactory)


class DocumentCreatorFactory(DjangoModelFactory):
    class Meta:
        model = DocumentCreator

    document = SubFactory(DocumentFactory)
    creator = SubFactory(DoctorFactory)


class DoctorSummaryFactory(DjangoModelFactory):
    class Meta:
        model = DoctorSummary

    doctor = SubFactory(DoctorFactory)
    short_summary = fake.text(max_nb_chars=1000)
    summary = fake.text(max_nb_chars=100000)
