from typing import Any, Optional

from django.core.management.base import BaseCommand
from faker import Faker
from ...tests.factories.user_app_factories import RoleFactory

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        RoleFactory(name="patient")
        RoleFactory(name="doctor")
