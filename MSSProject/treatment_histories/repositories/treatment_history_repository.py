from django.db.models import QuerySet, Q, Prefetch

from common.repository.base_repository import AbstractRepository
from ..models import TreatmentHistory, TreatmentHistoryImageForAnalyzes
from ..serializers import TreatmentHistorySerializer


class TreatmentHistoryRepository(AbstractRepository):
    def __init__(self):
        self.qs = TreatmentHistory.objects.select_related(
            "doctor",
            "doctor__user",
            "doctor__user__role",
            "patient",
            "patient__role",
        ).prefetch_related(
            Prefetch(
                "treatment_history_image_for_analyzes",
                queryset=TreatmentHistoryImageForAnalyzes.objects.select_related(
                    "treatment_history",
                    "image_for_analyzes",
                ).all(),
            ),
        )

    def list(self, **kwargs) -> QuerySet[TreatmentHistory]:
        ps = kwargs.get("patient_slug", None)
        ds_slug = kwargs.get("doctor_specialization_slug", None)
        if ds_slug is None:
            return self.qs.filter(patient__slug=ps)
        return self.qs.filter(
            Q(patient__slug=ps)
            & Q(
                doctor__doctor_doctor_specialization__doctor_specialization__slug=ds_slug
            )
        )

    def get(self, **kwargs) -> TreatmentHistory:
        th_slug = kwargs.get("treatment_history_slug", None)
        treatment_history = self.qs.get(slug=th_slug)
        return treatment_history

    def is_exist(self, **kwargs) -> bool:
        th_slug = kwargs.get("treatment_history_slug", None)
        if th_slug is not None:
            return TreatmentHistory.objects.filter(slug=th_slug).exists()

        date = kwargs.get("date", None)
        ps = kwargs.get("patient_slug", None)
        ds = kwargs.get("doctor_slug", None)
        if date is not None and ps is not None and ds is not None:
            return TreatmentHistory.objects.filter(
                Q(date=date) & Q(patient__user__slug=ps) & Q(doctor__user__slug=ds)
            ).exists()
        return False

    def create(self, data: dict) -> TreatmentHistory:
        serializer = TreatmentHistorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_valid(self, data: dict) -> bool:
        serializer = TreatmentHistorySerializer(data=data)
        return serializer.is_valid(raise_exception=True)

    def update(
        self, data: dict, treatment_history: TreatmentHistory
    ) -> TreatmentHistory:
        serializer = TreatmentHistorySerializer(
            instance=treatment_history, data=data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            count_of_updated_rows = serializer.save()
            if count_of_updated_rows == 1:
                return self.get(treatment_history_slug=treatment_history.slug)
