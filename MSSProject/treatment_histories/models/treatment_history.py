from __future__ import annotations
from django.db import models
from common.utils.string_utils import generate_slug_from_str

from datetime import datetime

# user app imports
from user.models import User

# doctor app imports
from doctor.models import Doctor


class TreatmentHistory(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField()
    conclusion = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # slug generation
        self.slug = generate_slug_from_str(self.patient.login) + generate_slug_from_str(
            self.doctor.user.login
        )
        # if slug already exist regenerate it
        while TreatmentHistory.objects.filter(slug=self.slug).exists():
            self.slug = generate_slug_from_str(
                self.patient.login
            ) + generate_slug_from_str(self.doctor.user.login)
        return super(TreatmentHistory, self).save(*args, **kwargs)

    class Meta:
        db_table = "treatment_history"

    def __str__(self) -> str:
        full_name_patient = (
            self.patient.userpersonalinfo.first_name
            + " "
            + self.patient.userpersonalinfo.second_name
            + " "
            + self.patient.userpersonalinfo.patronymic
        )
        full_name_doctor = (
            self.doctor.user.userpersonalinfo.first_name
            + " "
            + self.doctor.user.userpersonalinfo.second_name
            + " "
            + self.doctor.user.userpersonalinfo.patronymic
        )
        return self.title + " " + full_name_patient + " " + full_name_doctor
