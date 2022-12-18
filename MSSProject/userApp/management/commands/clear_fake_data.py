from typing import Any, Optional
from userApp.utils.image_utils import FolderController
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from ...models import (
    DoctorType,
    ImageForAnalyzes,
    Role,
    TreatmentHistory,
    User,
    UserDocumentType,
)


class Command(BaseCommand):
    help: str = "clear fake data from database tables"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        print(f"Roles models was deleted:{Role.objects.all().delete()}")
        print(
            f"Document types models was deleted:{ImageForAnalyzes.objects.all().delete()}"
        )
        print(f"Users models was deleted:{User.objects.all().delete()}")
        print(
            f"Treatments history models was deleted{TreatmentHistory.objects.all().delete()}"
        )
        print(f"Doctors types models was deleted:{DoctorType.objects.all().delete()}")
        print(f"Tokens models was deleted:{Token.objects.all().delete()}")
        print(
            f"UserDocuments type models was deleted:{UserDocumentType.objects.all().delete()}"
        )
        folder_controller = FolderController()
        folder_controller.remove_dir("media")
