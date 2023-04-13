from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        call_command("clear_fake_data")
        print("_____create_fake_users_______")
        call_command("create_fake_users")
        print("_____create_fake_doctors______")
        call_command("create_fake_doctors")
        print("______create_fake_documents______")
        call_command("create_fake_documents")
        print("_____create_fake_treatment_histories______")
        call_command("create_fake_treatment_histories")
        print("________create_fake_appointments________")
        call_command("create_fake_appointments")
