from django.db import models
from .user import User


class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = "user_location"
