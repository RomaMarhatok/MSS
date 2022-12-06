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
from ...utils.string_utls import generate_valid_password

fake = Faker()


class Command(BaseCommand):
    help: str = "create fake data from tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        patient_role = RoleFactory(name="patient")
        doctor_role = RoleFactory(name="doctor")
        for _ in range(1, 100):
            user = UserFactory(
                login=fake.pystr(),
                password=generate_valid_password(),
                role=patient_role,
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
                role=doctor_role,
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
