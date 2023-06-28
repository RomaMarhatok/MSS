from faker import Faker
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from ...models import Role, User
from ...tests.factories import (
    UserFactory,
    UserLocationFactory,
    UserPersonalInfoFactory,
    RoleFactory,
)


from common.utils.string_utils import generate_valid_login, generate_valid_password


fake = Faker(locale="ru_RU")


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        patient_role = RoleFactory(name=Role.PATIENT)
        doctor_role = RoleFactory(name=Role.DOCTOR)
        for _ in range(25):
            patient = self.generate_user(patient_role)
            self.generate_user_info(patient)
            doctor = self.generate_verified_user(doctor_role)
            self.generate_user_info(doctor)
        user = User.objects.last()
        user.login = "user"
        hashed_password = make_password("12345678")
        user.password = hashed_password
        user.verified = True
        user.role = patient_role
        user.save()
        self.create_super_user()

    def generate_user(self, role: Role) -> User:
        return UserFactory(
            login=generate_valid_login(),
            password=generate_valid_password(),
            role=role,
            verified=fake.pybool(),
        )

    def generate_verified_user(self, role: Role):
        return UserFactory(
            login=generate_valid_login(),
            password=generate_valid_password(),
            role=role,
            verified=True,
        )

    def generate_user_info(self, user: User) -> None:
        UserPersonalInfoFactory(
            user=user,
            first_name=fake.first_name(),
            second_name=fake.last_name(),
            patronymic=fake.last_name(),
            email=fake.email(),
            gender=fake.simple_profile()["sex"],
            age=fake.random_number(digits=2),
            health_status=fake.text(),
        )
        UserLocationFactory(
            user=user,
            country=fake.country(),
            city=fake.city(),
            address=fake.address(),
        )

    def create_super_user(self):
        if not User.objects.filter(is_superuser=True).exists():
            super_user = User.objects.create(
                login="admin",
                password="admin"
            )
            super_user.set_password("admin")
            super_user.is_superuser = True
            super_user.is_staff = True
            super_user.is_active = True
            super_user.save()
