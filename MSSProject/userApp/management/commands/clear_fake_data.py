from typing import Any, Optional
from userApp.utils.image_utils import FolderController
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from ...models import (
    DoctorSpecialization,
    ImageForAnalyzes,
    Role,
    TreatmentHistory,
    User,
    DocumentType,
    DocumentCreator,
)


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        print(f"Roles models was deleted:{Role.objects.all().delete()}")
        print(
            f"Document types models was deleted:{ImageForAnalyzes.objects.all().delete()}"
        )
        print(f"Users models was deleted:{User.objects.all().delete()}")
        print(
            f"Treatments history models was deleted{TreatmentHistory.objects.all().delete()}"
        )
        print(
            f"Doctors types models was deleted:{DoctorSpecialization.objects.all().delete()}"
        )
        print(f"Tokens models was deleted:{Token.objects.all().delete()}")
        print(
            f"UserDocuments type models was deleted:{DocumentType.objects.all().delete()}"
        )
        print(
            "UserDocumentsDoctor type models was"
            + f"deleted:{DocumentCreator.objects.all().delete()}"
        )
        folder_controller = FolderController()
        folder_controller.remove_dir("media")
