from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from django.http import HttpRequest
from common.permissions.is_user_authenticated import IsUserAuthenticated
from .services import DocumentTypeService, DocumentService


class DocumentTypeView(GenericViewSet):
    permission_classes = [AllowAny]
    lookup_field = "slug"
    service = DocumentTypeService()

    def list(self, request: HttpRequest):
        return self.service.get_all_document_types()


class DocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = DocumentService()

    def list(self, request: HttpRequest, user_slug=None):
        return self.service.get_document_list(user_slug)

    def retrieve(self, request, user_slug=None, doc_slug=None):
        return self.service.get_document(doc_slug, user_slug)
