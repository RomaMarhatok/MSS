from __future__ import annotations
from django.db import models
from .user import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "patient"

    def __str__(self) -> str:
        full_name_patient = (
            self.user.userpersonalinfo.first_name
            + " "
            + self.user.userpersonalinfo.second_name
            + " "
            + self.user.userpersonalinfo.patronymic
        )
        return full_name_patient
