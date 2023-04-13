from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import serializers
from django.http import HttpRequest
from common.permissions.is_user_authenticated import IsUserAuthenticated
from .services import DocumentTypeService, DocumentService


class DocumentTypeView(GenericViewSet):
    permission_classes = [AllowAny]
    lookup_field = "slug"
    service = DocumentTypeService()

    def list(self, request: HttpRequest):
        return self.service.get_all_document_types()


class NewestDocumentView(APIView):
    permission_classes = [IsUserAuthenticated]
    service = DocumentService()

    def get(self, request: HttpRequest, patient_slug: str):
        return self.service.get_newest_documents(patient_slug)


class DocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = DocumentService()

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        content = serializers.CharField()
        user_slug = serializers.SlugField()
        creator_slug = serializers.SlugField()
        document_type_slug = serializers.SlugField()

    def list(self, request: HttpRequest, user_slug=None):
        return self.service.get_document_list(user_slug)

    def retrieve(self, request, user_slug=None, doc_slug=None):
        return self.service.get_document(doc_slug, user_slug)

    def create(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_document(serializer.validated_data)
