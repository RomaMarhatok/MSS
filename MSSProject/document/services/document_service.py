from django.http import JsonResponse
from ..repositories import DocumentRepository
from ..serializers import DocumentSerializer
from responses.errors import JsonResponseBadRequest
from user.services.mixins.is_user_exist_mixin import IsUserExistMixin


class DocumentService(IsUserExistMixin):
    def __init__(self):
        self.document_repository: DocumentRepository = DocumentRepository()

    def get_document(self, document_slug: str, patient_slug: str) -> JsonResponse:
        response = self.user_exist(patient_slug)
        if response.status_code == 400:
            return response

        if not self.document_repository.is_exist(
            slug=document_slug, patient_slug=patient_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Документ не найден",
                    "description": "Документ с такими параметрами не существует",
                }
            )
        documents_qs = self.document_repository.get(
            slug=document_slug, patient_slug=patient_slug
        )
        documents = DocumentSerializer(
            instance=documents_qs,
        ).data
        return JsonResponse(data={"document": documents})

    def get_document_list(self, patient_slug: str) -> JsonResponse:
        response = self.user_exist(patient_slug)
        if response.status_code == 400:
            return response
        documents_qs = self.document_repository.list(patient_slug=patient_slug)
        documents = DocumentSerializer(
            instance=documents_qs, many=True, context={"repr": "list"}
        ).data
        return JsonResponse(data={"user_documents": documents})

    # TODO write tests,view,endpoints for api
    def newest_document(self, patient_slug: str):
        response = self.user_exist(patient_slug)
        if response.status_code == 400:
            return response

        documents_qs = self.document_repository.list(
            patient_slug=patient_slug
        ).order_by("created_at")[:5]
        documents = DocumentSerializer(
            instance=documents_qs, many=True, context={"repr": "list"}
        ).data
        return JsonResponse(data={"user_documents": documents})
