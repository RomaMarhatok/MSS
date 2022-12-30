from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from ..services.model_services.document_service import DocumentService


class DocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest, user_slug=None):
        document_service = DocumentService()
        data = document_service.get_all_documents(user_slug, include_context=True)
        return JsonResponse(
            data={"user_documents": data},
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, user_slug=None, doc_slug=None):
        document_service = DocumentService()
        data = document_service.get_document_data_by_slug(doc_slug, user_slug)
        return JsonResponse(data=data, status=status.HTTP_200_OK)
