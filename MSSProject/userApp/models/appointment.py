from django.db import models
from .doctor import Doctor
from .patient import Patient
from .doctor_specialization import DoctorSpecialization


class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_specialization = models.ForeignKey(
        DoctorSpecialization, on_delete=models.SET_NULL, null=True
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "appointments"
