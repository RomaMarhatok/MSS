from django.db.models import QuerySet
from ..models import DocumentType


class DocumentTypeRepository:
    def get_all(self) -> QuerySet[DocumentType]:
        return DocumentType.objects.all()
