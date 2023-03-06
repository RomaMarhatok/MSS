from __future__ import annotations
from django.db import models
from ..utils.slug_utils import generate_slug_from_str
from .doctor import Doctor
from .patient import Patient

# TODO add short description


class TreatmentHistory(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(
            self.patient.user.login
        ) + generate_slug_from_str(self.doctor.user.login)
        return super(TreatmentHistory, self).save(*args, **kwargs)

    class Meta:
        db_table = "treatment_history"
