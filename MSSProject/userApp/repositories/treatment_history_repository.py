from dataclasses import dataclass
from ..models import TreatmentHistory
from userApp.serializers.treatment_history_serializer import TreatmentHistorySerializer
from userApp.repositories.doctor_repository import DoctorRepository
from django.db.models import Q


@dataclass
class TreatmentHistoryRepository:
    doctor_repository: DoctorRepository = DoctorRepository()

    def get_treatments_histories(
        self, patient_slug: str, doctor_specialization_slug: str
    ):
        doctors_slugs = self.doctor_repository.get_doctors_by_specialization(
            doctor_specialization_slug
        )

        treatment_histories = TreatmentHistory.objects.filter(
            Q(patient__user__slug=patient_slug)
            & Q(doctor__user__slug__in=doctors_slugs)
        ).order_by("-date")
        serializer = TreatmentHistorySerializer(instance=treatment_histories, many=True)
        return serializer.data

    def get_treatment_history(self, patient_slug: str, treatment_slug: str) -> dict:
        treatment_history = (
            TreatmentHistory.objects.filter(
                patient__user__slug=patient_slug, slug=treatment_slug
            )
            .select_related("patient", "patient__user", "patient__user__role")
            .first()
        )
        serializer = TreatmentHistorySerializer(instance=treatment_history)
        return serializer.data

    def treatment_record_exist(self, treatment_slug: str):
        return TreatmentHistory.objects.filter(slug=treatment_slug).exists()
