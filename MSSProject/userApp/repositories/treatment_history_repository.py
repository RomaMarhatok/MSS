from dataclasses import dataclass
from .base import AbstractRepository
from ..models import TreatmentHistory
from userApp.serializers.treatment_history_serializer import TreatmentHistorySerializer
from userApp.repositories.doctor_repository import DoctorRepository
from django.db.models import QuerySet, Q


class TreatmentHistoryRepository(AbstractRepository):
    def __init__(self):
        self.doctor_repository = DoctorRepository()
        self.__init_query = TreatmentHistory.objects.select_related(
            "doctor",
            "doctor__user",
            "doctor__user__role",
            "patient",
            "patient__user",
            "patient__user__role",
        )

    def list(self, **kwargs) -> QuerySet[TreatmentHistory]:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_specialization_slug = kwargs.get("doctor_specialization_slug", None)
        if patient_slug is None or doctor_specialization_slug is None:
            return None
        doctors_slugs = [
            doctor.user.slug
            for doctor, _ in self.doctor_repository.list(
                doctor_specialization_slug=doctor_specialization_slug
            )
        ]
        print(doctors_slugs)
        treatment_histories = self.__init_query.filter(
            Q(patient__user__slug=patient_slug)
            & Q(doctor__user__slug__in=doctors_slugs)
        ).order_by("-date")
        return treatment_histories

    def get(self, **kwargs) -> TreatmentHistory:
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        patient_slug = kwargs.get("patient_slug", None)
        if patient_slug is None or treatment_history_slug is None:
            return None
        treatment_history = self.__init_query.get(
            Q(patient__user__slug=patient_slug) & Q(slug=treatment_history_slug)
        )
        return treatment_history

    def is_exist(self, **kwargs) -> bool:
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        if treatment_history_slug is None:
            return False
        return TreatmentHistory.objects.filter(slug=treatment_history_slug).exists()

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
