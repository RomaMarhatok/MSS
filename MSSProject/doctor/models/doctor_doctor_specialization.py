from django.db import models
from .doctor import Doctor
from .doctor_specialization import DoctorSpecialization


class DoctorDoctorSpecialization(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name="doctor_doctor_specialization", on_delete=models.CASCADE
    )
    doctor_specialization = models.ForeignKey(
        DoctorSpecialization,
        related_name="doctor_doctor_specialization",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "doctor_doctor_specialization"
        verbose_name = "Специализация доктора - Доктор"
        verbose_name_plural = "Специализации докторов - Доктора"
