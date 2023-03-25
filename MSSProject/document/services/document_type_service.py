from dataclasses import dataclass
from ..repositories import DocumentTypeRepository
from ..serializers import DocumentTypeSerializer


@dataclass
class DocumentTypeService:

    document_type_repository: DocumentTypeRepository = DocumentTypeRepository()

    def get_all_document_types(self) -> dict:
        data = DocumentTypeSerializer(
            instance=self.document_type_repository.list(), many=True
        ).data
        return {"document_types": data}
