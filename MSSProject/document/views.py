from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import serializers
from django.http import HttpRequest
from common.permissions.is_user_authenticated import IsUserAuthenticated
from common.permissions.is_doctor import IsDoctor
from .services import DocumentTypeService, DocumentService, DocumentDoctorService


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
        return self.service.get_patient_newest_documents(patient_slug)


class PatientDocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = DocumentService()

    def list(self, request: HttpRequest, user_slug=None):
        return self.service.get_patient_document_list(user_slug)

    def retrieve(self, request, user_slug=None, doc_slug=None):
        return self.service.get_patient_document(doc_slug, user_slug)


class DoctorDocumentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DocumentDoctorService()

    def list(self, request: HttpRequest, creator_slug=None):
        return self.service.get_doctor_document_list(creator_slug)

    def retrieve(self, request, creator_slug=None, doc_slug=None):
        return self.service.get_doctor_document(doc_slug, creator_slug)

    class CreateInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        content = serializers.CharField()
        user_slug = serializers.SlugField()
        creator_slug = serializers.SlugField()
        document_type_slug = serializers.SlugField()

    def create(self, request):
        serializer = self.CreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_document(serializer.validated_data)

    class UpdateInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        content = serializers.CharField()
        document_slug = serializers.SlugField()
        creator_slug = serializers.SlugField()
        document_type_slug = serializers.SlugField()

    def update(self, request):
        serializer = self.UpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.update_document(serializer.validated_data)

    class DeleteInputSerializer(serializers.Serializer):
        document_slug = serializers.SlugField()
        creator_slug = serializers.SlugField()

    def delete(self, request):
        serializer = self.DeleteInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.delete_document(serializer.validated_data)
