from rest_framework import status
from ..repositories import DocumentRepository
from ..serializers import DocumentSerializer


class DocumentService:
    def __init__(self):
        self.document_repository: DocumentRepository = DocumentRepository()

    def get_document_info(self, document_slug: str, patient_slug: str):
        document_creator = self.document_repository.get(
            slug=document_slug, patient_slug=patient_slug
        )
        data = DocumentSerializer(
            instance=document_creator,
            context={"include_context": True},
        ).data
        return {"data": data, "status": status.HTTP_200_OK}

    def get_all_documents_with_content(self, patient_slug: str):
        data = DocumentSerializer(
            instance=self.document_repository.list(patient_slug=patient_slug),
            many=True,
            context={"include_context": True},
        ).data
        return {"data": {"user_documents": data}, "status": status.HTTP_200_OK}

    def get_all_documents_without_content(self, patient_slug: str):
        data = DocumentSerializer(
            instance=self.document_repository.list(patient_slug=patient_slug),
            many=True,
            context={"include_context": False},
        ).data
        return {"data": {"user_documents": data}, "status": status.HTTP_200_OK}
