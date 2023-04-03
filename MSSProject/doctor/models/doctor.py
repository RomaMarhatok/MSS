from django.db import models

# user app import
from user.models import User


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
