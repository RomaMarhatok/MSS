from faker import Faker
import random
from typing import Any, Optional
from django.core.management.base import BaseCommand
from document.models import DocumentType
from document.tests.factories import DocumentTypeFactory, DocumentFactory

# user app imports
from user.models import User, Role

# doctor app imports
from doctor.models import Doctor

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        document_types = self.generate_document_types()
        users = User.objects.filter(role__name=Role.PATIENT)
        doctors = Doctor.objects.all()
        for user, doctor in zip(users, doctors):
            for _ in range(15):
                DocumentFactory(
                    name=fake.pystr(),
                    content=fake.text(max_nb_chars=10000),
                    user=user,
                    creator=doctor,
                    document_type=random.choice(document_types),
                )

    def generate_document_types(self):
        test = DocumentTypeFactory(name=DocumentType.TEST)
        analyzes = DocumentTypeFactory(name=DocumentType.ANALYZES)
        conclusions = DocumentTypeFactory(name=DocumentType.CONCLUSIONS)
        return [test, analyzes, conclusions]
