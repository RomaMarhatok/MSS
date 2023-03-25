from django.db import models
from common.utils.string_utils import generate_slug_from_str


class DocumentType(models.Model):
    TEST = "TEST"
    ANALYZES = "ANALYZES"
    CONCLUSIONS = "CONCLUSIONS"

    DOCUMENT_TYPE_CHOICES = (
        (TEST, "Test"),
        (ANALYZES, "Analyzes"),
        (CONCLUSIONS, "Conclusions"),
    )

    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=255, choices=DOCUMENT_TYPE_CHOICES)

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(DocumentType, self).save(*args, **kwargs)

    class Meta:
        db_table = "document_type"

    def __str__(self) -> str:
        return self.name
