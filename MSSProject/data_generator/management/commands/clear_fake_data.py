from typing import Any, Optional
from common.utils.image_utils import FolderController
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

# user app imports
from user.models import Role, User

# doctor app imports
from doctor.models import Doctor, DoctorSpecialization

# treatment_histories app imports
from treatment_histories.models import TreatmentHistory, ImageForAnalyzes

# documents app imports
from document.models import Document, DocumentType


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
        print(f"Doctors models was deleted:{Doctor.objects.all().delete()}")

        print(f"Tokens models was deleted:{Token.objects.all().delete()}")
        print(f"Documents models was deleted:{Document.objects.all().delete()}")
        print(
            f"Documents type models was deleted:{DocumentType.objects.all().delete()}"
        )
        folder_controller = FolderController()
        folder_controller.remove_dir("media")
