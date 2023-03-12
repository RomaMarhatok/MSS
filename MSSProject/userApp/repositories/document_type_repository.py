from django.db.models import QuerySet
from ..models import DocumentType
from .base import AbstractRepository


class DocumentTypeRepository(AbstractRepository):
    def list(self, **kwargs) -> QuerySet[DocumentType]:
        return DocumentType.objects.all()

    def get(self, **kwargs):
        return super().get(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        return super().is_exist(**kwargs)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
