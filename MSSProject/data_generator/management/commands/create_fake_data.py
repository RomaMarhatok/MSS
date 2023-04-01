from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        call_command("create_fake_users")
        call_command("create_fake_doctors")
        call_command("create_fake_documents")
        call_command("create_fake_treatment_histories")
        call_command("create_fake_appointments")
