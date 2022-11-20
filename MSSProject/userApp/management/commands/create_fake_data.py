from typing import Any, Optional

from django.core.management.base import BaseCommand
from faker import Faker

from ...tests.factories.document_type_factory import DocumentTypeFactory
from ...tests.factories.role_factory import RoleFactory
from ...tests.factories.user_document_factory import UserDocumentFactory
from ...tests.factories.user_factory import UserFactory
from ...tests.factories.user_personal_info_factory import \
    UserPersonalInfoFactory

fake = Faker()


class Command(BaseCommand):
    help: str = "create fake data from tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        for _ in range(100):
            role = RoleFactory(name=fake.pystr())
            user = UserFactory(
                username=fake.profile()["username"],
                login=fake.pystr(),
                password=fake.password(),
                role=role,
            )
            document_type = DocumentTypeFactory(document_type=fake.pystr())
            UserPersonalInfoFactory(
                user=user,
                image=fake.image_url(),
                first_name=fake.first_name(),
                second_name=fake.last_name(),
                patronymic=fake.last_name(),
                email=fake.email(),
            )
            UserDocumentFactory(content=fake.pystr(), doctype=document_type, user=user)
