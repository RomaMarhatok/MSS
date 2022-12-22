from ...models import UserDocument, UserDocumentDoctor
from ...serializers.user_serializer import UserDocumentSerializer
from ...services.model_services.doctor_service import DoctorService


class DocumentService:
    def get_document_data_by_slug(self, document_slug: str, user_slug: str):
        user_document = UserDocument.objects.filter(
            slug=document_slug, user__slug=user_slug
        ).first()
        doctor = (
            UserDocumentDoctor.objects.filter(user_document=user_document)
            .first()
            .doctor
        )
        doctor_service = DoctorService()
        doctor_info = doctor_service.get_doctor_info(doctor.user.slug)
        serializer = UserDocumentSerializer(instance=user_document)
        return {
            "user_document": serializer.data,
            "doctor_creator": doctor_info,
        }

    def get_all_documents(self, user_slug: str, include_context: bool = False):
        user_documents = UserDocument.objects.filter(user__slug=user_slug)
        serializer = UserDocumentSerializer(
            instance=user_documents,
            many=True,
            context={"include_context": include_context},
        )
        return serializer.data
