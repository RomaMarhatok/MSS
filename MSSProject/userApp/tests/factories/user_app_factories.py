from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

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

    name = fake.pystr()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("role",)

    login = fake.pystr()
    password = fake.password()
    role = SubFactory(RoleFactory)


class UserPersonalInfoFactory(DjangoModelFactory):
    class Meta:
        model = UserPersonalInfo
        django_get_or_create = ("user",)

    user = SubFactory(UserFactory)
    image = fake.image_url()
    first_name = fake.first_name()
    second_name = fake.last_name()
    patronymic = fake.last_name()
    email = fake.email()


class UserDocumentFactory(DjangoModelFactory):
    class Meta:
        model = UserDocument
        django_get_or_create = ("user",)

    content = fake.text()
    user = SubFactory(UserFactory)


class DoctorTypesFactory(DjangoModelFactory):
    class Meta:
        model = DoctorType

    doctor_type = fake.pystr()


class DoctorFactory(DjangoModelFactory):
    class Meta:
        model = Doctor
        django_get_or_create = ("user",)

    user = SubFactory(UserFactory)


class DoctorDoctorTypesFactory(DjangoModelFactory):
    class Meta:
        model = DoctorDoctorTypes

    doctor = SubFactory(DoctorFactory)
    doctor_type = SubFactory(DoctorType)


class PatinesFactory(DjangoModelFactory):
    class Meta:
        model = Patient
        django_get_or_create = ("user",)

    user = SubFactory(UserFactory)


class ImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = ImageForAnalyzes

    image = fake.image_url()
    description = fake.text()


class TreatmentsHistoryFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistory
        django_get_or_create = ("doctor", "patient")

    description = fake.text()
    doctor = SubFactory(DoctorFactory)
    patient = SubFactory(Patient)


class TreatmentHistoryImageForAnalyzesFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentHistoryImageForAnalyzes
        django_get_or_create = ("treatment_history", "image_for_analyzes")

    treatment_history = SubFactory(TreatmentHistory)
    image_for_analyzes = SubFactory(ImageForAnalyzes)
