from __future__ import annotations
from django.db import models
from .user import User


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("first name", max_length=100)
    second_name = models.CharField("second name", max_length=100)
    patronymic = models.CharField("patronymic", max_length=100, blank=True)
    email = models.EmailField("email", max_length=100, blank=True)
    gender = models.CharField(max_length=150, blank=True, default="Other")
    age = models.IntegerField(blank=True, default=-1)
    health_status = models.TextField(blank=True, default="")

    class Meta:
        db_table = "user_personal_info"
        verbose_name = "Персональная информация пользователя"
        verbose_name_plural = "Персональная информация пользователей"

    def __str__(self) -> str:
        return self.first_name + " " + self.second_name + " " + self.patronymic

    @property
    def full_name(self):
        return self.first_name + " " + self.second_name + " " + self.patronymic
