from typing import Any, Optional

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import DocumentType, Roles, User


class Command(BaseCommand):
    help: str = "clear fake data from database tables"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        print(f"Roles model was deleted:{Roles.objects.all().delete()}")
        print(f"Document types was deleted:{DocumentType.objects.all().delete()}")
        print(f"Users model was deleted:{User.objects.all().delete()}")
