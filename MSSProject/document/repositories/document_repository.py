from django.db.models import Q, QuerySet
from ..models import Document
from common.repository.base_repository import AbstractRepository
from ..serializers import DocumentSerializer


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
        creator_slug = kwargs.get("creator_slug", None)
        if patient_slug is not None:
            return self.qs.filter(user__slug=patient_slug)
        if creator_slug is not None:
            return self.qs.filter(creator__user__slug=creator_slug)

    def create(self, data: dict) -> Document:
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs) -> int:
        document_slug = kwargs.get("document_slug", None)
        creator_slug = kwargs.get("creator_slug", None)
        return Document.objects.filter(
            Q(slug=document_slug) & Q(creator__user__slug=creator_slug)
        ).delete()

    def is_exist(self, **kwargs) -> bool:
        slug = kwargs.get("slug", None)
        patient_slug = kwargs.get("patient_slug", None)
        document_name = kwargs.get("document_name", None)
        creator_slug = kwargs.get("creator_slug", None)
        if patient_slug is not None and slug is not None:
            return self.qs.filter(Q(slug=slug) & Q(user__slug=patient_slug)).exists()
        if creator_slug is not None and slug is not None:
            return self.qs.filter(
                Q(slug=slug) & Q(creator__user__slug=creator_slug)
            ).exists()
        if slug is not None:
            return self.qs.filter(slug=slug).exists()
        if patient_slug is not None:
            return self.qs.filter(user__slug=patient_slug).exists()
        if document_name is not None:
            return self.qs.filter(name=document_name).exists()

    def update(self, data: dict, document: Document) -> Document:
        serializer = DocumentSerializer(instance=document, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            count_of_updated_rows = serializer.save()
            if count_of_updated_rows == 1:
                return self.get(slug=document.slug)
