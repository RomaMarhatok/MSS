from dataclasses import dataclass
from django.http import JsonResponse
from ..repositories import DocumentTypeRepository
from ..serializers import DocumentTypeSerializer


@dataclass
class DocumentTypeService:

    document_type_repository: DocumentTypeRepository = DocumentTypeRepository()

    def get_all_document_types(self) -> JsonResponse:
        data = DocumentTypeSerializer(
            instance=self.document_type_repository.list(), many=True
        ).data
        return JsonResponse(data={"document_types": data})
