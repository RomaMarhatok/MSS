from django.db import models
from .document import Document
from .doctor import Doctor


class DocumentCreator(models.Model):
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "document_creator"

    def __str__(self) -> str:
        full_name = (
            self.creator.user.userpersonalinfo.first_name
            + " "
            + self.creator.user.userpersonalinfo.second_name
            + " "
            + self.creator.user.userpersonalinfo.patronymic
        )
        return self.document.name + " " + full_name
