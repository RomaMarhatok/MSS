from dataclasses import dataclass
from ...repositories.document_type_repository import DocumentTypeRepository
from ...serializers.document_type_serializer import DocumentTypeSerializer


@dataclass
class DocumentTypeService:

    document_type_repository: DocumentTypeRepository = DocumentTypeRepository()

    def get_all_document_types(self) -> dict:
        instances = self.document_type_repository.get_all()
        return {
            "document_types": DocumentTypeSerializer(instance=instances, many=True).data
        }
