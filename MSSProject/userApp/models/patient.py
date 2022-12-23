from __future__ import annotations
from django.db import models
from .user import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "patient"
