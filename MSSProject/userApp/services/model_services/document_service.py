from ...models import Document, DocumentCreator
from ...serializers.document_serializer import DocumentSerializer
from ...services.model_services.doctor_service import DoctorService


class DocumentService:
    def get_document_data_by_slug(self, document_slug: str, user_slug: str):
        user_document = Document.objects.filter(
            slug=document_slug, user__slug=user_slug
        ).first()
        doctor = (
            DocumentCreator.objects.filter(user_document=user_document).first().creator
        )
        doctor_service = DoctorService()
        doctor_info = doctor_service.get_doctor_by_slug(doctor.user.slug)
        serializer = DocumentSerializer(instance=user_document)
        return {
            "user_document": serializer.data,
            "doctor_creator": doctor_info,
        }

    def get_all_documents(self, user_slug: str, include_context: bool = False):
        user_documents = Document.objects.filter(user__slug=user_slug)
        serializer = DocumentSerializer(
            instance=user_documents,
            many=True,
            context={"include_context": include_context},
        )
        return serializer.data
