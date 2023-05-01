from django.db import models
from document.models.document import Document
from ..models import TreatmentHistory


class TreatmentHistoryDocument(models.Model):
    treatment_history = models.ForeignKey(
        TreatmentHistory,
        on_delete=models.CASCADE,
        related_name="treatment_history_document",
        related_query_name="treatment_history_document",
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="treatment_history_document",
        related_query_name="treatment_history_document",
    )

    class Meta:
        db_table = "treatment_history_document"
        verbose_name = "Прилогающийся документ"
        verbose_name_plural = "Прилогающиеся документы"
