from typing import Any, Optional

from django.core.management.base import BaseCommand
from faker import Faker
from ...utils.image_utils import load_image_from_url_to_file
from ...tests.factories.user_app_factories import (
    DoctorFactory,
    DoctorTypesFactory,
    ImageForAnalyzesFactory,
    PatinesFactory,
    RoleFactory,
    TreatmentsHistoryFactory,
    UserDocumentFactory,
    UserFactory,
    UserPersonalInfoFactory,
    DoctorDoctorTypesFactory,
    TreatmentHistoryImageForAnalyzesFactory,
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

            doctor = DoctorFactory(user=doctor_user)
            DoctorDoctorTypesFactory(doctor=doctor, doctor_type=doctor_type)
            patient = PatinesFactory(user=user)

            img_for_analyzes = ImageForAnalyzesFactory(
                image=fake.image_url(),
                description=fake.text(),
            )
            treatment = TreatmentsHistoryFactory(
                description=fake.text(),
                doctor=doctor,
                patient=patient,
            )
            TreatmentHistoryImageForAnalyzesFactory(
                treatment_history=treatment, image_for_analyzes=img_for_analyzes
            )
