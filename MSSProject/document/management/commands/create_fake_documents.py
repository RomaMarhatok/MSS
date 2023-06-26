from faker import Faker
import random
from typing import Any, Optional
from django.core.management.base import BaseCommand
from document.enums import BaseDocumentTypesEnum
from document.tests.factories import DocumentTypeFactory, DocumentFactory

# user app imports
from user.models import User, Role

# doctor app imports
from doctor.models import Doctor

fake = Faker(locale="ru_RU")


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        document_types = self.generate_document_types()
        users = User.objects.filter(role__name=Role.PATIENT)
        doctors = Doctor.objects.all()
        for user in users:
            for _ in range(15):
                DocumentFactory(
                    name=fake.pystr(),
                    content=fake.text(max_nb_chars=1000),
                    user=user,
                    creator=random.choice(doctors),
                    document_type=random.choice(document_types),
                )

    def generate_document_types(self):
        test = DocumentTypeFactory(name=BaseDocumentTypesEnum.TEST.value)
        analyzes = DocumentTypeFactory(name=BaseDocumentTypesEnum.ANALYZE.value)
        conclusions = DocumentTypeFactory(name=BaseDocumentTypesEnum.CONCLUSION.value)
        return [test, analyzes, conclusions]
