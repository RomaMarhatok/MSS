from django.db import models
from ..utils.slug_utils import generate_slug_from_str


class Role(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField("role name", max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(Role, self).save(*args, **kwargs)

    class Meta:
        db_table = "role"
