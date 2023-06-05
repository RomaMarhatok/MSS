from common.repository.base_repository import AbstractRepository
from ..serializers import TreatmentHistoryImageForAnalyzesSerializer
from ..models import (
    TreatmentHistoryImageForAnalyzes,
    TreatmentHistory,
    ImageForAnalyzes,
)


class TreatmentHistoryImageForAnalyzesRepository(AbstractRepository):
    def get(self, **kwargs):
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        image_for_analyzes_slug = kwargs.get("image_for_analyzes_slug", None)
        return TreatmentHistoryImageForAnalyzes.objects.get(
            treatment_history__slug=treatment_history_slug,
            image_for_analyzes__slug=image_for_analyzes_slug,
        )

    def list(self, **kwargs):
        super().list(**kwargs)

    def create(
        self, treatment_history: TreatmentHistory, image_for_analyzes: ImageForAnalyzes
    ) -> TreatmentHistoryImageForAnalyzes:
        return TreatmentHistoryImageForAnalyzes.objects.create(
            treatment_history=treatment_history,
            image_for_analyzes=image_for_analyzes,
        )

    def delete(self, **kwargs):
        ts = kwargs.get("ts", None)
        img = kwargs.get("img", None)
        return TreatmentHistoryImageForAnalyzes.objects.filter(
            treatment_history=ts, image_for_analyzes=img
        ).delete()

    def is_exist(self, **kwargs) -> bool:
        super().is_exist(**kwargs)
