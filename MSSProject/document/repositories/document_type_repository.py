from django.db.models import QuerySet
from ..models import DocumentType
from common.repository.base_repository import AbstractRepository


class DocumentTypeRepository(AbstractRepository):
    def list(self, **kwargs) -> QuerySet[DocumentType]:
        return DocumentType.objects.all()

    def get(self, **kwargs):
        name = kwargs.get("name", None)
        if name is not None:
            return DocumentType.objects.get(name=name)
        slug = kwargs.get("slug", None)
        if slug is not None:
            return DocumentType.objects.get(slug=slug)

    def is_exist(self, **kwargs) -> bool:
        return super().is_exist(**kwargs)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
