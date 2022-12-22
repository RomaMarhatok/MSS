from typing import Any, Optional
import random
from django.core.management.base import BaseCommand
from faker import Faker
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
    UserDocumentTypeFactory,
    UserLocationFactory,
    UserDocumentDoctorFactory,
)
from ...utils.string_utls import generate_valid_password, generate_valid_login
from ...utils.image_utils import load_image_from_url

fake = Faker()


class Command(BaseCommand):
    help: str = "create fake data from tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        patient_role, doctor_role = self.prepare_roles()
        document_types = self.prepare_documents_types()
        for _ in range(1, 25):

            user = UserFactory(
                login=generate_valid_login(),
                password=generate_valid_password(),
                role=patient_role,
            )
            UserPersonalInfoFactory(
                user=user,
                image=load_image_from_url(fake.image_url()),
                first_name=fake.first_name(),
                second_name=fake.last_name(),
                patronymic=fake.last_name(),
                email=fake.email(),
                gender=fake.simple_profile()["sex"],
                age=fake.random_number(digits=2),
                health_status=fake.text(),
            )
            UserLocationFactory(
                user=user,
                country=fake.country(),
                city=fake.city(),
                address=fake.address(),
            )
            doctor_user = UserFactory(
                username=fake.profile()["username"],
                login=generate_valid_login(),
                password=generate_valid_password(),
                role=doctor_role,
            )
            UserPersonalInfoFactory(
                user=doctor_user,
                image=load_image_from_url(fake.image_url()),
                first_name=fake.first_name(),
                second_name=fake.last_name(),
                patronymic=fake.last_name(),
                email=fake.email(),
                gender=fake.simple_profile()["sex"],
                age=fake.random_number(digits=2),
                health_status=fake.text(),
            )
            doctor = DoctorFactory(user=doctor_user)

            self.create_user_documents(user, document_types, doctor)
            doctor_type = DoctorTypesFactory(doctor_type=fake.pystr())

            DoctorDoctorTypesFactory(doctor=doctor, doctor_type=doctor_type)
            patient = PatinesFactory(user=user)

            img_for_analyzes = ImageForAnalyzesFactory(
                image=load_image_from_url(fake.image_url()),
                description=fake.text(max_nb_chars=10000),
            )
            treatment = TreatmentsHistoryFactory(
                description=fake.text(max_nb_chars=10000),
                doctor=doctor,
                patient=patient,
            )
            TreatmentHistoryImageForAnalyzesFactory(
                treatment_history=treatment, image_for_analyzes=img_for_analyzes
            )

    def create_user_documents(self, user, document_types, doctor):
        for _ in range(50):
            user_document = UserDocumentFactory(
                name=fake.pystr(),
                content=fake.text(max_nb_chars=10000),
                user=user,
                document_type=random.choice(document_types),
            )
            UserDocumentDoctorFactory(user_document=user_document, doctor=doctor)

    def prepare_roles(self):
        patient_role = RoleFactory(name="patient")
        doctor_role = RoleFactory(name="doctor")
        return (
            patient_role,
            doctor_role,
        )

    def prepare_documents_types(self):
        test = UserDocumentTypeFactory(name="test")
        analyzes = UserDocumentTypeFactory(name="analyzes")
        conclusions = UserDocumentTypeFactory(name="conclusions")
        return [test, analyzes, conclusions]
