import random
from datetime import datetime, timedelta
from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...tests.factories import AppointmentsFactory

# user app imports
from user.models import User, Role

# doctor app imports
from doctor.models import Doctor, DoctorDoctorSpecialization

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.PATIENT)
        doctors = Doctor.objects.all()
        for user, doctor in zip(users, doctors):
            for _ in range(random.randint(1, 15)):
                AppointmentsFactory(
                    patient=random.choice(users),
                    doctor=doctor,
                    date=fake.date_time_between(
                        start_date=datetime.now(),
                        end_date=datetime.now() + timedelta(days=300),
                    ),
                    doctor_specialization=random.choice(
                        self.get_doctor_specializations(doctor)
                    ),
                )
            AppointmentsFactory(
                patient=user,
                doctor=doctor,
                date=fake.date_time_between(
                    start_date=datetime.now(),
                    end_date=datetime.now() + timedelta(days=300),
                ),
                doctor_specialization=random.choice(
                    self.get_doctor_specializations(doctor)
                ),
            )

    def get_doctor_specializations(self, doctor: Doctor):
        specializations = [
            doctor_doctor_specialization.doctor_specialization
            for doctor_doctor_specialization in DoctorDoctorSpecialization.objects.filter(
                doctor=doctor
            )
        ]
        return specializations
