from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ...models import (
    Doctor,
    DoctorType,
    ImageForAnalyzes,
    Patient,
    Roles,
    TreatmentHistory,
    User,
    UserDocument,
    UserPersonalInfo,
)

fake = Faker()


class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Roles

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


class DoctorsFactory(DjangoModelFactory):
    class Meta:
        model = Doctor
        django_get_or_create = ("user",)

    user = SubFactory(UserFactory)
    doctor_type = SubFactory(DoctorTypesFactory)


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
        django_get_or_create = ("doctor", "patient", "image")

    description = fake.text()
    doctor = SubFactory(DoctorsFactory)
    patient = SubFactory(Patient)
    image = SubFactory(ImageForAnalyzesFactory)
