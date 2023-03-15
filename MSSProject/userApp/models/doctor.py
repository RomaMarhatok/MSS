from django.db import models
from .user import User


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"

    def __str__(self) -> str:
        return self.user.login
