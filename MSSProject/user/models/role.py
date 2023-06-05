from django.db import models
from common.utils.string_utils import generate_slug_from_str


class Role(models.Model):
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"
    ROLE_CHOICES = (
        (DOCTOR, "Doctor"),
        (PATIENT, "Patient"),
    )
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(
        "role name", choices=ROLE_CHOICES, max_length=100, unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(Role, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "role"
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
