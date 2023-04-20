from common.repository.base_repository import AbstractRepository
from ..serializers import TreatmentHistoryImageForAnalyzesSerializer
from ..models import TreatmentHistoryImageForAnalyzes


class TreatmentHistoryImageForAnalyzesRepository(AbstractRepository):
    def get(self, **kwargs):
        super().get(**kwargs)

    def list(self, **kwargs):
        super().list(**kwargs)

    def create(self, data: dict) -> TreatmentHistoryImageForAnalyzes:
        treatment_history = data.get("treatment_history", None)
        image_for_analyzes = data.get("image_for_analyzes", None)
        TreatmentHistoryImageForAnalyzes.objects.create(
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
