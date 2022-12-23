from django.db import models
from ..utils.slug_utils import generate_slug_from_str


class DoctorSpecialization(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField("doctor profession name", max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(DoctorSpecialization, self).save(*args, **kwargs)

    class Meta:
        db_table = "doctor_specialization"
