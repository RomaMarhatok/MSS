import random
import os
from faker import Faker
from ..providers.doctor_specialization_provider import DoctorSpecializationProvider
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...models import Doctor, DoctorSpecialization
from ...tests.factories import (
    DoctorFactory,
    DoctorSummaryFactory,
    DoctorSpecializationFactory,
    DoctorDoctorSpecializationFactory,
)
from django.contrib.auth.hashers import make_password


# user app imports
from user.models import User, Role

fake = Faker(locale="ru_RU")
fake.add_provider(DoctorSpecializationProvider)


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.DOCTOR)
        self.generate_doctor_specialization_names()
        for user in users:
            doctor = DoctorFactory(user=user)
            DoctorSummaryFactory(
                doctor=doctor,
                short_summary=fake.text(max_nb_chars=100),
                summary=fake.text(max_nb_chars=1000),
            )
            self.generate_doctor_specializations(doctor)
        doctor = Doctor.objects.last()
        doctor.user.login = "doctor"
        salt = os.environ.get("HASHER_SALT", None)
        hashed_password = make_password("12345678", salt=salt)
        doctor.user.password = hashed_password
        doctor.user.verified = True
        doctor.user.save()
        doctor.save()

    def generate_doctor_specializations(self, doctor: Doctor):
        doctor_specialization = random.choice(DoctorSpecialization.objects.all())
        DoctorDoctorSpecializationFactory(
            doctor=doctor, doctor_specialization=doctor_specialization
        )

    def generate_doctor_specialization_names(self):
        for i in DoctorSpecializationProvider.doctor_specializations:
            DoctorSpecializationFactory(name=i)
