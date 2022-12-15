from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from ..serializers.user_serializer import UserDocumentSerializer
from ..models import UserDocument
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from ..models import User


class DocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest, user_slug=None):
        user_docuements = UserDocument.objects.filter(user__slug=user_slug)
        print(user_docuements.count())
        serializer = UserDocumentSerializer(instance=user_docuements, many=True)
        return JsonResponse(
            data={"user_documents": serializer.data},
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, user_slug=None, doc_slug=None):
        user_document = UserDocument.objects.filter(
            slug=doc_slug, user__slug=user_slug
        ).first()
        serializer = UserDocumentSerializer(instance=user_document)
        return JsonResponse(
            data={"user_document": serializer.data}, status=status.HTTP_200_OK
        )
