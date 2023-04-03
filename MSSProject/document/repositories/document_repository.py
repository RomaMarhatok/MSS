from django.db.models import Q, QuerySet
from ..models import Document
from common.repository.base_repository import AbstractRepository


class DocumentRepository(AbstractRepository):
    def __init__(self):
        self.__init_query = Document.objects.select_related(
            "creator",
            "document",
            "document__document_type",
            "document__user",
            "document__user__role",
            "creator__user",
            "creator__user__role",
        )

    def get(self, **kwargs) -> None | Document:
        slug = kwargs.get("slug", None)
        patient_slug = kwargs.get("patient_slug", None)
        if slug is None and patient_slug is None:
            return None
        try:
            if patient_slug is not None and slug is not None:
                return self.__init_query.get(
                    Q(document__slug=slug) & Q(document__user__slug=patient_slug)
                )
            if slug is not None:
                return self.__init_query.get(document__slug=slug)
            if patient_slug is not None:
                return self.__init_query.get(document__user__slug=patient_slug)
        except Document.DoesNotExist:
            return None
        except Document.MultipleObjectsReturned:
            return None

    def list(self, **kwargs) -> QuerySet[Document]:
        patient_slug = kwargs.get("patient_slug", None)
        if patient_slug is not None:
            return self.__init_query.filter(document__user__slug=patient_slug)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        return super().is_exist(**kwargs)