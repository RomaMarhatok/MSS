from typing import Any, Optional
import random
from django.core.management.base import BaseCommand
from faker import Faker
from ...tests.factories.user_app_factories import (
    DoctorFactory,
    DoctorSpecializationFactory,
    ImageForAnalyzesFactory,
    PatinesFactory,
    RoleFactory,
    TreatmentsHistoryFactory,
    DocumentFactory,
    UserFactory,
    UserPersonalInfoFactory,
    DoctorDoctorSpecializationFactory,
    TreatmentHistoryImageForAnalyzesFactory,
    DocumentTypeFactory,
    UserLocationFactory,
    DocumentCreatorFactory,
)
from ...utils.string_utls import generate_valid_password, generate_valid_login
from ...utils.image_utils import load_image_from_url
from enum import Enum

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        patient_role, doctor_role = self.prepare_roles()
        document_types = self.prepare_documents_types()
        for i in range(1, 25):
            print(f"{i*4}%")
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
            self.prepare_doctor_specializations(doctor)
            self.create_user_documents(user, document_types, doctor)

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
            document = DocumentFactory(
                name=fake.pystr(),
                content=fake.text(max_nb_chars=10000),
                user=user,
                document_type=random.choice(document_types),
            )
            DocumentCreatorFactory(document=document, creator=doctor)

    def prepare_roles(self):
        patient_role = RoleFactory(name="patient")
        doctor_role = RoleFactory(name="doctor")
        return (
            patient_role,
            doctor_role,
        )

    def prepare_documents_types(self):
        test = DocumentTypeFactory(name="test")
        analyzes = DocumentTypeFactory(name="analyzes")
        conclusions = DocumentTypeFactory(name="conclusions")
        return [test, analyzes, conclusions]

    def prepare_doctor_specializations(self, doctor):
        for _ in range(random.randint(1, 5)):
            doctor_specialization = DoctorSpecializationFactory(name=fake.pystr())
            DoctorDoctorSpecializationFactory(
                doctor=doctor, doctor_specialization=doctor_specialization
            )
