from django.db import models
from user.models import User
from common.utils.string_utils import generate_slug_from_str


class PhysicalParameters(models.Model):
    slug = models.SlugField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    pressure = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "physical_parameters"

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.user.slug)
        return super().save(*args, **kwargs)
