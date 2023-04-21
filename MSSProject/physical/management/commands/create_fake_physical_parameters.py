import random
from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...test.factories import PhysicalParametersFactory
from user.models import User, Role

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.PATIENT)
        for user in users:
            for _ in range(random.randint(1, 30)):
                PhysicalParametersFactory(
                    user=user,
                    weight=round(random.uniform(60, 300), 2),
                    height=round(random.uniform(100, 250), 2),
                    pressure=round(random.uniform(60, 250), 2),
                )
