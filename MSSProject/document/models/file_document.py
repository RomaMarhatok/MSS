from unidecode import unidecode
from datetime import datetime
from django.db import models

from user.models import User
from doctor.models import Doctor
from common.utils.string_utils import generate_slug_from_str, generate_hash_from_string
from ..models import DocumentType


def media_path_builder_for_documents(instance, filename):
    now_date = datetime.now().strftime("%Y/%m/%d")
    return "/".join(
        [
            "media_files",
            "documents",
            now_date,
            filename,
        ]
    )


class FileDocument(models.Model):
    slug = models.SlugField(max_length=200)
    name = models.CharField(max_length=300)
    document = models.FileField(upload_to=media_path_builder_for_documents)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "file_document"

    def save(self, *args, **kwargs) -> None:
        name = self.document.name.split(".")[0]
        ext = self.document.name.split(".")[1]
        self.name = name
        self.document.name = generate_hash_from_string(unidecode(name)) + "." + ext
        self.slug = generate_slug_from_str(unidecode(name))
        return super(FileDocument, self).save(*args, **kwargs)
