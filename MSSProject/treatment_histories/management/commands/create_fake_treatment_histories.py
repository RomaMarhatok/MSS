import random
from datetime import datetime, timedelta
from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...tests.factories import (
    ImageForAnalyzesFactory,
    TreatmentHistoryFactory,
    TreatmentHistoryImageForAnalyzesFactory,
)
from common.utils.image_utils import load_image_from_url

# user app imports
from user.models import User, Role

# doctor app imports
from doctor.models import Doctor

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.PATIENT)
        doctors = Doctor.objects.all()
        for user, doctor in zip(users, doctors):
            for _ in range(random.randint(1, 10)):
                img_for_analyzes = ImageForAnalyzesFactory(
                    image=load_image_from_url(fake.image_url()),
                    description=fake.text(max_nb_chars=100),
                )
                treatment = TreatmentHistoryFactory(
                    title=fake.text(max_nb_chars=100),
                    short_description=fake.text(max_nb_chars=100),
                    description=fake.text(max_nb_chars=1000),
                    conclusion=fake.text(max_nb_chars=100),
                    date=fake.date_time_between(
                        start_date=datetime.now(),
                        end_date=datetime.now() + timedelta(days=300),
                    ),
                    doctor=doctor,
                    patient=user,
                )
                TreatmentHistoryImageForAnalyzesFactory(
                    treatment_history=treatment, image_for_analyzes=img_for_analyzes
                )
