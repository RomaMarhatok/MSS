from dataclasses import dataclass
from ..models.treatment_history import TreatmentHistory
from userApp.serializers.treatment_history_serializer import TreatmentHistorySerializer


@dataclass
class TreatmentHistoryRepository:
    def get_treatments_histories_for_patient(self, patient_slug: str) -> list[dict]:
        treatment_histories = TreatmentHistory.objects.filter(
            patient__user__slug=patient_slug
        ).select_related("patient", "patient__user")
        serializer = TreatmentHistorySerializer(instance=treatment_histories, many=True)
        return serializer.data

    def get_treatment_history_for_patient(
        self, patient_slug: str, treatment_slug: str
    ) -> dict:
        treatment_history = TreatmentHistory.objects.filter(
            patient__user__slug=patient_slug, slug=treatment_slug
        ).first()
        serializer = TreatmentHistorySerializer(instance=treatment_history)
        return serializer.data

    def treatment_record_exist(self, treatment_slug: str):
        return TreatmentHistory.objects.filter(slug=treatment_slug).exists()
