from typing import Any, Optional

from django.core.management.base import BaseCommand
from faker import Faker

from ...tests.factories.user_app_factories import (
    DoctorsFactory,
    DoctorTypesFactory,
    ImageForAnalyzesFactory,
    PatinesFactory,
    RoleFactory,
    TreatmentsHistoryFactory,
    UserDocumentFactory,
    UserFactory,
    UserPersonalInfoFactory,
)

fake = Faker()


class Command(BaseCommand):
    help: str = "create fake data from tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        for _ in range(100):
            role = RoleFactory(name=fake.pystr())
            user = UserFactory(
                login=fake.pystr(),
                password=fake.password(),
                role=role,
            )
            UserPersonalInfoFactory(
                user=user,
                image=fake.image_url(),
                first_name=fake.first_name(),
                second_name=fake.last_name(),
                patronymic=fake.last_name(),
                email=fake.email(),
            )
            UserDocumentFactory(content=fake.pystr(), user=user)
            doctor_type = DoctorTypesFactory(doctor_type=fake.pystr())

            doctor_user = UserFactory(
                username=fake.profile()["username"],
                login=fake.pystr(),
                password=fake.password(),
                role=role,
            )

            doctor = DoctorsFactory(user=doctor_user, doctor_type=doctor_type)
            patient = PatinesFactory(user=user)

            img_for_analyzes = ImageForAnalyzesFactory(
                image=fake.image_url(), description=fake.text()
            )
            TreatmentsHistoryFactory(
                description=fake.text(),
                doctor=doctor,
                patient=patient,
                image=img_for_analyzes,
            )
