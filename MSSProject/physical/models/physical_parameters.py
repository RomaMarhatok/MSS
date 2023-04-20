from django.db import models
from user.models import User


class PhysicalParameters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    pressure = models.FloatField()

    class Meta:
        db_table = "physical_parameters"
