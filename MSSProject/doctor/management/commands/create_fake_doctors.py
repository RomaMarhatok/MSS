import random
from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...models import Doctor
from ...tests.factories import (
    DoctorFactory,
    DoctorSummaryFactory,
    DoctorSpecializationFactory,
    DoctorDoctorSpecializationFactory,
)


# user app imports
from user.models import User, Role

fake = Faker(locale="ru_RU")


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.DOCTOR)
        for user in users:
            doctor = DoctorFactory(user=user)
            DoctorSummaryFactory(
                doctor=doctor,
                short_summary=fake.text(max_nb_chars=100),
                summary=fake.text(max_nb_chars=1000),
            )
            self.generate_doctor_specializations(doctor)

    def generate_doctor_specializations(self, doctor: Doctor):
        for _ in range(random.randint(1, 5)):
            doctor_specialization = DoctorSpecializationFactory(name=fake.pystr())
            DoctorDoctorSpecializationFactory(
                doctor=doctor, doctor_specialization=doctor_specialization
            )
