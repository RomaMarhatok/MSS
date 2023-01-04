from django.db.models import Q, QuerySet
from .mapper.mapper import Mapper
from dataclasses import dataclass
from ..models import Document, DocumentCreator
from ..serializers.doctor_serializer import DoctorSerializer
from ..serializers.document_serializer import DocumentSerializer
from ..models import DocumentType, Doctor, User


@dataclass
class DocumentRepository:
    function_mapper: Mapper = Mapper()

    def get_all_user_documents(
        self, user_slug, serialized=False, include_context=False
    ) -> QuerySet[Document] | list[dict]:
        documents = Document.objects.filter(user__slug=user_slug).select_related(
            "document_type", "user", "user__role"
        )
        serialized_documents = DocumentSerializer(
            instance=documents, many=True, context={"include_context": include_context}
        ).data
        return serialized_documents if serialized else documents

    def get_document_by(self, serialized=False, **kwargs) -> Document | dict:
        function_map = {
            ("slug",): self.get_document_by_slug,
            (
                "document_slug",
                "user_slug",
            ): self.get_document_by_document_slug_user_slug,
        }
        document = (
            self.function_mapper.mapping(function_map, kwargs=kwargs)
            .select_related("user", "user__role", "document_type")
            .first()
        )

        serialized_instance = DocumentSerializer(instance=document).data
        return serialized_instance if serialized else document

    def get_document_by_slug(self, slug) -> QuerySet[Document]:
        return Document.objects.filter(slug=slug)

    def get_document_by_document_slug_user_slug(
        self, document_slug, user_slug
    ) -> QuerySet[Document]:
        return Document.objects.filter(Q(slug=document_slug) & Q(user__slug=user_slug))

    def get_document_creator(
        self, document_slug: str, serilized=False
    ) -> Document | dict:
        creator = (
            DocumentCreator.objects.filter(document__slug=document_slug)
            .select_related("creator", "creator__user", "creator__user__role")
            .first()
            .creator
        )
        serialized_data = DoctorSerializer(instance=creator).data
        return serialized_data if serilized else creator
