from dataclasses import dataclass
from django.http import JsonResponse
from ..repositories import DocumentTypeRepository
from ..serializers import DocumentTypeSerializer


@dataclass
class DocumentTypeService:

    document_type_repository: DocumentTypeRepository = DocumentTypeRepository()

    def get_all_document_types(self) -> JsonResponse:
        document_types_qs = self.document_type_repository.list()
        document_types = DocumentTypeSerializer(
            instance=document_types_qs, many=True
        ).data
        return JsonResponse(data={"document_types": document_types})
