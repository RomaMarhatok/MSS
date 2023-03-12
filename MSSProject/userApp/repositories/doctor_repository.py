from .base import AbstractRepository
from ..models import DoctorDoctorSpecialization, Doctor
from django.db.models import QuerySet, Prefetch


class DoctorRepository(AbstractRepository):
    def __init__(self):
        self.__init_query_set = Doctor.objects.select_related(
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

    def get(
        self, **kwargs
    ) -> tuple[Doctor, QuerySet[DoctorDoctorSpecialization]] | None:
        slug = kwargs.get("slug", None)
        if slug is None:
            return None
        doctor = self.__init_query_set.get(user__slug=slug)
        return (doctor, doctor.doctor_doctor_specialization.all())

    def list(
        self, **kwargs
    ) -> list[tuple[Doctor, QuerySet[DoctorDoctorSpecialization]]]:
        doctor_specialization_slug = kwargs.get("doctor_specialization_slug", None)
        if doctor_specialization_slug is not None:
            query_result = []
            for doctor in self.__init_query_set.all():
                if doctor.doctor_doctor_specialization.filter(
                    doctor_specialization__slug=doctor_specialization_slug
                ).exists():
                    query_result.append(
                        (
                            doctor,
                            doctor.doctor_doctor_specialization.all(),
                        )
                    )
            return query_result

        return [
            (
                doctor,
                doctor.doctor_doctor_specialization.all(),
            )
            for doctor in self.__init_query_set.all()
        ]

    def is_exist(self, **kwargs) -> bool:
        slug = kwargs.get("slug", None)
        if slug is None:
            return False
        return DoctorDoctorSpecialization.objects.filter(
            doctor__user__slug=slug
        ).exists()

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
