from django.http import JsonResponse
from ..repositories import DocumentRepository
from ..serializers import DocumentSerializer
from responses.errors import JsonResponseNotFound


class DocumentService:
    def __init__(self):
        self.document_repository: DocumentRepository = DocumentRepository()

    def get_document(self, document_slug: str, patient_slug: str) -> JsonResponse:
        if not self.document_repository.is_exist(
            slug=document_slug, patient_slug=patient_slug
        ):
            return JsonResponseNotFound(
                data={
                    "message": "Документ не найден",
                    "description": "Документ с такими параметрами не существует",
                }
            )
        document = self.document_repository.get(
            slug=document_slug, patient_slug=patient_slug
        )
        if document is not None:
            data = DocumentSerializer(
                instance=document,
            ).data
            return JsonResponse(data={"document": data})

    def get_document_list(self, patient_slug: str) -> JsonResponse:

        data = DocumentSerializer(
            instance=self.document_repository.list(patient_slug=patient_slug),
            many=True,
            context={"repr": "list"},
        ).data
        return JsonResponse(data={"user_documents": data})
