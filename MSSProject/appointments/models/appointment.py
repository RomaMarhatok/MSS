from django.db import models

# user app imports
from user.models import User

# doctor app imports
from doctor.models import Doctor, DoctorSpecialization


class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_specialization = models.ForeignKey(
        DoctorSpecialization, on_delete=models.SET_NULL, null=True
    )
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "appointments"
        verbose_name = "Запись к врачу"
        verbose_name_plural = "Записи к врачам"

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
        return full_name_doctor + " " + full_name_patient
