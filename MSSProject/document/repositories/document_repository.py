from django.db.models import Q, QuerySet
from ..models import Document
from common.repository.base_repository import AbstractRepository


class DocumentRepository(AbstractRepository):
    def __init__(self):
        self.qs = Document.objects.select_related(
            "user",
            "user__role",
            "user__userpersonalinfo",
            "document_type",
            "creator__user",
            "creator__user__role",
            "creator__user__userpersonalinfo",
        )

    def get(self, **kwargs) -> Document:
        slug = kwargs.get("slug", None)
        patient_slug = kwargs.get("patient_slug", None)
        if patient_slug is not None and slug is not None:
            return self.qs.get(Q(slug=slug) & Q(user__slug=patient_slug))
        if slug is not None:
            return self.qs.get(slug=slug)
        if patient_slug is not None:
            return self.qs.get(user__slug=patient_slug)

    def list(self, **kwargs) -> QuerySet[Document]:
        patient_slug = kwargs.get("patient_slug", None)
        if patient_slug is not None:
            return self.qs.filter(user__slug=patient_slug)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        slug = kwargs.get("slug", None)
        patient_slug = kwargs.get("patient_slug", None)
        if slug is None and patient_slug is None:
            return None
        if patient_slug is not None and slug is not None:
            return self.qs.filter(Q(slug=slug) & Q(user__slug=patient_slug)).exists()
        if slug is not None:
            return self.qs.filter(slug=slug).exists()
        if patient_slug is not None:
            return self.qs.filter(user__slug=patient_slug).exists()
