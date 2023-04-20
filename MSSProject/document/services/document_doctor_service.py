from django.http import JsonResponse
from django.db import transaction
from ..repositories import DocumentRepository, DocumentTypeRepository
from ..serializers import DocumentSerializer
from responses.errors import JsonResponseBadRequest
from user.services.mixins.is_user_exist_mixin import IsUserExistMixin
from doctor.repositories import DoctorRepository


class DocumentDoctorService(IsUserExistMixin):
    def __init__(self):
        self.document_repository: DocumentRepository = DocumentRepository()
        self.doctor_repository: DoctorRepository = DoctorRepository()
        self.document_type_repository: DocumentTypeRepository = DocumentTypeRepository()

    def get_doctor_document(self, document_slug, creator_slug):
        self.is_user_exist(creator_slug)

        if not self.document_repository.is_exist(
            slug=document_slug, creator_slug=creator_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Документ не найден",
                    "description": "Документ с такими параметрами не существует",
                }
            )
        documents_qs = self.document_repository.get(
            slug=document_slug, creator_slug=creator_slug
        )
        documents = DocumentSerializer(
            instance=documents_qs,
        ).data
        return JsonResponse(data={"doctor_document": documents})

    def get_doctor_document_list(self, creator_slug: str) -> JsonResponse:
        self.is_user_exist(creator_slug)
        documents_qs = self.document_repository.list(creator_slug=creator_slug)
        documents = DocumentSerializer(
            instance=documents_qs, many=True, context={"repr": "list"}
        ).data
        return JsonResponse(data={"doctor_documents": documents})

    @transaction.atomic
    def create_document(self, data: dict):
        user_slug = data.get("user_slug", None)
        self.is_user_exist(user_slug)
        creator_slug = data.get("creator_slug", None)
        self.is_user_exist(creator_slug)
        document_name = data.get("name", None)
        if self.document_repository.is_exist(document_name=document_name):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Документ с таким название уже существует",
                }
            )

        document_qs = self.document_repository.create(data)
        serialized_document = DocumentSerializer(instance=document_qs).data
        return JsonResponse(data=serialized_document)

    @transaction.atomic
    def delete_document(self, data: dict):
        document_slug = data.get("document_slug", None)
        creator_slug = data.get("creator_slug", None)
        self.is_user_exist(creator_slug)
        if not self.document_repository.is_exist(
            slug=document_slug, creator_slug=creator_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Документ не найден",
                    "description": "Документ с такими параметрами не существует",
                }
            )
        count_of_deleted_instances = self.document_repository.delete(
            document_slug=document_slug, creator_slug=creator_slug
        )
        if bool(count_of_deleted_instances):
            return JsonResponse(
                data={
                    "deleted_document_slug": document_slug,
                    "creator_slug": creator_slug,
                }
            )

    @transaction.atomic
    def update_document(self, data: dict):
        document_slug = data.get("document_slug", None)
        creator_slug = data.get("creator_slug", None)
        if not self.document_repository.is_exist(
            slug=document_slug, creator_slug=creator_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Документ не найден",
                    "description": "Документ с такими параметрами не существует",
                }
            )
        document_qs = self.document_repository.get(slug=document_slug)
        document = self.document_repository.update(data, document_qs)
        serializes_document = DocumentSerializer(instance=document).data
        return JsonResponse(data={"document": serializes_document})
