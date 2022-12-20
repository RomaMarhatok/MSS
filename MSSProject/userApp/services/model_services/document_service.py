from ...models import UserDocument
from ...serializers.user_serializer import UserDocumentSerializer


class DocumentService:
    def get_document_data_by_slug(self, document_slug: str, user_slug: str):
        user_document = UserDocument.objects.filter(
            slug=document_slug, user__slug=user_slug
        ).first()
        serializer = UserDocumentSerializer(instance=user_document)
        return serializer.data

    def get_all_documents(self, user_slug: str, include_context: bool = False):
        user_documents = UserDocument.objects.filter(user__slug=user_slug)
        serializer = UserDocumentSerializer(
            instance=user_documents,
            many=True,
            context={"include_context": include_context},
        )
        return serializer.data
