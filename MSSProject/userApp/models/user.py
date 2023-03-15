from django.db import models
from ..utils.slug_utils import generate_slug_from_str
from django.contrib.auth.models import AbstractUser
from .role import Role


class User(AbstractUser):
    slug = models.SlugField(max_length=100, unique=True)
    login = models.CharField("user login", max_length=100, unique=True)
    password = models.CharField("user password", max_length=100)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.login)
        self.username = self.login
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.login
