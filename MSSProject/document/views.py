from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from common.permissions.is_user_authenticated import IsUserAuthenticated
from .services import DocumentTypeService, DocumentService


class DocumentTypeView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest):
        document_type_service = DocumentTypeService()
        data = document_type_service.get_all_document_types()
        return JsonResponse(
            data=data,
            status=status.HTTP_200_OK,
        )


class DocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest, user_slug=None):
        document_service = DocumentService()
        data = document_service.get_all_documents_with_content(user_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(self, request, user_slug=None, doc_slug=None):
        document_service = DocumentService()
        data = document_service.get_document_info(doc_slug, user_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )
