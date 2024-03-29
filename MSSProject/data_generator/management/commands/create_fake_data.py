from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.core.management import call_command
from user.models import User


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        if not User.objects.filter(login="user").exists() and not User.objects.filter(login="doctor").exists():
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
            print("________create_physical_parameters________")
            call_command("create_fake_physical_parameters")
