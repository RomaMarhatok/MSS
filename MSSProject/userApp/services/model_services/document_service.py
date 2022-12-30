from ...models import Document, DocumentCreator
from ...serializers.document_serializer import DocumentSerializer
from ...services.model_services.doctor_service import DoctorService
from ...serializers.document_creator_serializer import DocumentCreatorSerializer


class DocumentService:
    def get_document_data_by_slug(self, document_slug: str, user_slug: str):
        user_document = Document.objects.filter(
            slug=document_slug, user__slug=user_slug
        ).first()
        document_creator = DocumentCreator.objects.filter(
            document=user_document
        ).first()
        doctor_service = DoctorService()
        creator_data = doctor_service.get_serializet_doctor(document_creator.creator)
        document = DocumentCreatorSerializer(instance=document_creator).data["document"]
        return {
            "document": document,
            "creator": {"slug": creator_data["doctor_slug"]},
        }

    def get_all_documents(self, user_slug: str, include_context: bool = False):
        user_documents = Document.objects.filter(user__slug=user_slug)
        serializer = DocumentSerializer(
            instance=user_documents,
            many=True,
            context={"include_context": include_context},
        )
        return serializer.data
