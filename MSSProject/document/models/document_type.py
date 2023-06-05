from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class DocumentType(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=255, unique=True)
    unicode_name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.unicode_name = unidecode(self.name)
        self.slug = slugify(self.unicode_name, allow_unicode=True)
        return super(DocumentType, self).save(*args, **kwargs)

    class Meta:
        db_table = "document_type"
        verbose_name = "Тип документа"
        verbose_name_plural = "Типы документа"

    def __str__(self) -> str:
        return self.name
