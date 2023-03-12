from django.db.models import Q, QuerySet
from ..models import DocumentCreator
from ..serializers.doctor_serializer import DoctorSerializer
from ..serializers.document_serializer import DocumentSerializer
from ..serializers.document_creator_serializer import DocumentCreatorSerializer
from .base import AbstractRepository


class DocumentRepository(AbstractRepository):
    def __init__(self):
        self.__init_query = DocumentCreator.objects.select_related(
            "creator",
            "document",
            "document__document_type",
            "document__user",
            "document__user__role",
            "creator__user",
            "creator__user__role",
        )

    def get(self, **kwargs) -> None | DocumentCreator:
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
        except DocumentCreator.DoesNotExist:
            return None
        except DocumentCreator.MultipleObjectsReturned:
            return None

    def list(self, **kwargs) -> QuerySet[DocumentCreator]:
        patient_slug = kwargs.get("patient_slug", None)
        if patient_slug is not None:
            return self.__init_query.filter(document__user__slug=patient_slug)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        return super().is_exist(**kwargs)


# class DocumentRepository:
#     def get_patient_documents(
#         self, user_slug, serialized=False, include_context=False
#     ) -> QuerySet[Document] | list[dict]:
#         documents_creators = DocumentCreator.objects.filter(
#             document__user__slug=user_slug
#         ).select_related(
#             "creator",
#             "document",
#             "document__document_type",
#             "document__user",
#             "document__user__role",
#             "creator__user",
#             "creator__user__role",
#         )
#         serialized_documents_creators = DocumentCreatorSerializer(
#             instance=documents_creators,
#             many=True,
#             context={"include_context": include_context},
#         ).data
#         return serialized_documents_creators if serialized else documents_creators

#     def get_document_by(self, serialized=False, **kwargs) -> Document | dict:
#         function_map = {
#             ("slug",): self.get_document_by_slug,
#             (
#                 "document_slug",
#                 "user_slug",
#             ): self.get_document_by_document_slug_user_slug,
#         }
#         document = (
#             self.function_mapper.mapping(function_map, kwargs=kwargs)
#             .select_related("user", "user__role", "document_type")
#             .first()
#         )

#         serialized_instance = DocumentSerializer(instance=document).data
#         return serialized_instance if serialized else document

#     def get_document_by_slug(self, slug) -> QuerySet[Document]:
#         return Document.objects.filter(slug=slug)

#     def get_document_by_document_slug_user_slug(
#         self, document_slug, user_slug
#     ) -> QuerySet[Document]:
#         return Document.objects.filter(Q(slug=document_slug) & Q(user__slug=user_slug))

#     def get_document_creator(
#         self, document_slug: str, serilized=False
#     ) -> Document | dict:
#         creator = (
#             DocumentCreator.objects.filter(document__slug=document_slug)
#             .select_related("creator", "creator__user", "creator__user__role")
#             .first()
#             .creator
#         )
#         serialized_data = DoctorSerializer(instance=creator).data
#         return serialized_data if serilized else creator
