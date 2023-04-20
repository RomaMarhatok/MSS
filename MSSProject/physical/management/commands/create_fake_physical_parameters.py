import random
from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from ...test.factories import PhysicalParametersFactory
from user.models import User, Role

# doctor app imports
from doctor.models import Doctor

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.filter(role__name=Role.PATIENT)
        for user in users:
            for _ in range(random.randint(1, 30)):
                PhysicalParametersFactory(
                    user=user,
                    weight=fake.pyfloat(positive=True, min_value=60.0),
                    height=fake.pyfloat(positive=True, min_value=100.0),
                    pressure=fake.pyfloat(positive=True, min_value=120.0),
                )
