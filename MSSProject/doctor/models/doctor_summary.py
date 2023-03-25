from django.db import models
from .doctor import Doctor


class DoctorSummary(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    short_summary = models.TextField()
    summary = models.TextField()

    class Meta:
        db_table = "doctor_summary"
