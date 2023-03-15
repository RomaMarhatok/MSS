from django.db import models
from .document_type import DocumentType
from .user import User
from ..utils.slug_utils import generate_slug_from_str


class Document(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    content = models.TextField("document content")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_document"

    def save(self, *args, **kwargs):
        self.slug = generate_slug_from_str(self.name)
        return super(Document, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
