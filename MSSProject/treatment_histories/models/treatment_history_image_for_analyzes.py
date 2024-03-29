from django.db import models
from .treatment_history import TreatmentHistory
from .image_for_analyzes import ImageForAnalyzes


class TreatmentHistoryImageForAnalyzes(models.Model):
    treatment_history = models.ForeignKey(
        TreatmentHistory,
        related_name="treatment_history_image_for_analyzes",
        related_query_name="treatment_history_image_for_analyzes",
        on_delete=models.CASCADE,
    )
    image_for_analyzes = models.ForeignKey(
        ImageForAnalyzes,
        related_name="treatment_history_image_for_analyzes",
        related_query_name="treatment_history_image_for_analyzes",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "treatment_history_image_for_analyzes"
        verbose_name = "Прилогающиеся изображение"
        verbose_name_plural = "Прилогающиеся изображения"
