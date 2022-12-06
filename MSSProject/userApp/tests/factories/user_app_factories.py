from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from ...utils.string_utls import generate_valid_password
from ...models import (
    Doctor,
    DoctorType,
    ImageForAnalyzes,
    Patient,
    Role,
    TreatmentHistory,
    User,
    UserDocument,
    UserPersonalInfo,
    DoctorDoctorTypes,
    TreatmentHistoryImageForAnalyzes,
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

    login = fake.pystr()
    password = generate_valid_password()
    role = SubFactory(RoleFactory)


class UserPersonalInfoFactory(DjangoModelFactory):
    class Meta:
        model = UserPersonalInfo

    user = SubFactory(UserFactory)
    image = fake.image_url()
    first_name = fake.first_name()
    second_name = fake.last_name()
    patronymic = fake.last_name()
    email = fake.email()


class UserDocumentFactory(DjangoModelFactory):
    class Meta:
        model = UserDocument

    content = fake.text()
    user = SubFactory(UserFactory)


class DoctorTypesFactory(DjangoModelFactory):
    class Meta:
        model = DoctorType

    doctor_type = fake.pystr()


class DoctorFactory(DjangoModelFactory):
    class Meta:
        model = Doctor

    user = SubFactory(UserFactory)


class DoctorDoctorTypesFactory(DjangoModelFactory):
    class Meta:
        model = DoctorDoctorTypes

    doctor = SubFactory(DoctorFactory)
    doctor_type = SubFactory(DoctorType)


class PatinesFactory(DjangoModelFactory):
    class Meta:
        model = Patient

    user = SubFactory(UserFactory)


class ImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = ImageForAnalyzes

    image = fake.image_url()
    description = fake.text()


class TreatmentsHistoryFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistory

    description = fake.text()
    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(Patient)


class TreatmentHistoryImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistoryImageForAnalyzes

    treatment_history = SubFactory(TreatmentHistory)
    image_for_analyzes = SubFactory(ImageForAnalyzes)
