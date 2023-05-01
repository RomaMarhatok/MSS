from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from .role import Role

from common.utils.string_utils import generate_slug_from_str


class User(AbstractUser):
    slug = models.SlugField(max_length=100, unique=True)
    login = models.CharField("user login", max_length=100, unique=True)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.login)
        if self.login is not None and self.login:
            self.username = self.login
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.login
