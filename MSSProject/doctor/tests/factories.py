from factory import SubFactory
from factory.django import DjangoModelFactory
from ..models import (
    Doctor,
    DoctorSummary,
    DoctorSpecialization,
    DoctorDoctorSpecialization,
)
from faker import Faker

# user app import
from user.tests.factories import UserFactory

fake = Faker(locale="ru_RU")


class DoctorFactory(DjangoModelFactory):
    class Meta:
        model = Doctor

    user = SubFactory(UserFactory)


class DoctorSummaryFactory(DjangoModelFactory):
    class Meta:
        model = DoctorSummary

    doctor = SubFactory(DoctorFactory)
    short_summary = fake.text(max_nb_chars=1000)
    summary = fake.text(max_nb_chars=100000)


class DoctorSpecializationFactory(DjangoModelFactory):
    class Meta:
        model = DoctorSpecialization

    name = fake.pystr()


class DoctorDoctorSpecializationFactory(DjangoModelFactory):
    class Meta:
        model = DoctorDoctorSpecialization

    doctor = SubFactory(DoctorFactory)
    doctor_specialization = SubFactory(DoctorSpecializationFactory)
