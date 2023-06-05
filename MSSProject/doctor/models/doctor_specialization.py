from unidecode import unidecode
from django.db import models
from common.utils.string_utils import generate_slug_from_str


class DoctorSpecialization(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField("doctor profession name", max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(unidecode(self.name))
        return super(DoctorSpecialization, self).save(*args, **kwargs)

    class Meta:
        db_table = "doctor_specialization"
        verbose_name = "Специализация доктора"
        verbose_name_plural = "Специализации докторов"

    def __str__(self) -> str:
        return self.name
