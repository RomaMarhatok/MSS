import random
from datetime import datetime, timedelta
from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...tests.factories import (
    ImageForAnalyzesFactory,
    TreatmentHistoryFactory,
    TreatmentHistoryImageForAnalyzesFactory,
    TreatmentHistoryDocumentFactory,
)
from common.utils.image_utils import load_image_from_url

# user app imports
from user.models import User, Role

# doctor app imports
from doctor.models import Doctor

from document.models import Document

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.PATIENT)
        doctors = Doctor.objects.all()
        for user, doctor in zip(users, doctors):
            for _ in range(random.randint(1, 10)):
                treatment_history = TreatmentHistoryFactory(
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
                images_for_analyzes = self.create_images()
                self.create_union_table(treatment_history, images_for_analyzes)
                self.create_treatment_history_documents(doctor, treatment_history)

    def create_images(self):
        return [
            ImageForAnalyzesFactory(
                image=load_image_from_url(fake.image_url()),
                description=fake.text(max_nb_chars=100),
            )
            for _ in range(random.randint(1, 10))
        ]

    def create_union_table(self, treatment_history, images_for_analyzes):
        for image_for_analyze in images_for_analyzes:
            TreatmentHistoryImageForAnalyzesFactory(
                treatment_history=treatment_history,
                image_for_analyzes=image_for_analyze,
            )

    def create_treatment_history_documents(self, doctor: Doctor, treatment_history):
        documents = Document.objects.filter(creator=doctor)
        for _ in range(random.randint(1, 10)):
            TreatmentHistoryDocumentFactory(
                treatment_history=treatment_history, document=random.choice(documents)
            )
