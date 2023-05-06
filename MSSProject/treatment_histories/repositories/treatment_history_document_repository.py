from common.repository.base_repository import AbstractRepository
from ..models import TreatmentHistoryDocument


class TreatmentHistoryDocumentRepository(AbstractRepository):
    def list(self, **kwargs):
        pass

    def get(self, **kwargs):
        pass

    def is_exist(self, **kwargs) -> bool:
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        document_slug = kwargs.get("document_slug", None)
        return TreatmentHistoryDocument.objects.filter(
            treatment_history__slug=treatment_history_slug,
            document__slug=document_slug,
        ).exists()

    def create(self, data: dict) -> TreatmentHistoryDocument:
        treatment_history = data.get("treatment_history", None)
        document = data.get("document", None)
        return TreatmentHistoryDocument.objects.create(
            treatment_history=treatment_history, document=document
        )

    def delete(self, **kwargs) -> int:
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        document_slug = kwargs.get("document_slug", None)
        return TreatmentHistoryDocument.objects.filter(
            treatment_history__slug=treatment_history_slug,
            document__slug=document_slug,
        ).delete()
