from django.db import models
from ..utils.slug_utils import generate_slug_from_str


class DocumentType(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(DocumentType, self).save(*args, **kwargs)

    class Meta:
        db_table = "document_type"
