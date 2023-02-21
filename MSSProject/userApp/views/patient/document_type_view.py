from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ...permissions.is_user_authenticated import IsUserAuthenticated
from ...services.model_services.document_type_service import DocumentTypeService


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
