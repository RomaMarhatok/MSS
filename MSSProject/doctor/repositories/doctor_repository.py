from common.repository.base_repository import AbstractRepository
from ..models import DoctorDoctorSpecialization, Doctor
from django.db.models import QuerySet, Prefetch


class DoctorRepository(AbstractRepository):
    def __init__(self):
        self.qs = Doctor.objects.select_related(
            "user",
            "user__role",
            "user__userpersonalinfo",
            "user__userlocation",
            "doctorsummary",
        ).prefetch_related(
            Prefetch(
                "doctor_doctor_specialization",
                queryset=DoctorDoctorSpecialization.objects.select_related(
                    "doctor_specialization", "doctor"
                ),
            )
        )

    def get(self, **kwargs) -> Doctor:
        slug = kwargs.get("slug", None)
        doctor = self.qs.get(user__slug=slug)
        return doctor

    def list(self, **kwargs) -> QuerySet[Doctor]:
        return self.qs.all()

    def is_exist(self, **kwargs) -> bool:
        slug = kwargs.get("slug", None)
        if slug is None:
            return False
        return Doctor.objects.filter(user__slug=slug).exists()

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
