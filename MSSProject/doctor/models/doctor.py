from django.db import models

# user app import
from user.models import User


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self) -> str:
        return self.user.login
