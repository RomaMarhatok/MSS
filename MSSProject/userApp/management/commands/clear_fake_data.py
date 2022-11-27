from typing import Any, Optional

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import (DoctorTypes, ImageForAnalyzes, Roles, TreatmentsHistory,
                       User)


class Command(BaseCommand):
    help: str = "clear fake data from database tables"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        print(f"Roles models was deleted:{Roles.objects.all().delete()}")
        print(
            f"Document types models was deleted:{ImageForAnalyzes.objects.all().delete()}"
        )
        print(f"Users models was deleted:{User.objects.all().delete()}")
        print(
            f"Treatments history models was deleted{TreatmentsHistory.objects.all().delete()}"
        )
        print(f"Doctors types models was deleted:{DoctorTypes.objects.all().delete()}")
