from django.db import models
from .treatment_history import TreatmentHistory
from .image_for_analyzes import ImageForAnalyzes


class TreatmentHistoryImageForAnalyzes(models.Model):
    treatment_history = models.ForeignKey(TreatmentHistory, on_delete=models.CASCADE)
    image_for_analyzes = models.ForeignKey(ImageForAnalyzes, on_delete=models.CASCADE)

    class Meta:
        db_table = "treatment_history_image_for_analyzes"
