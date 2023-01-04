from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from ..services.model_services.doctor_specialization_service import DoctorTypeService


class DoctorSpecializationView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest):
        doctor_service = DoctorTypeService()
        data = doctor_service.get_doctor_types()
        return JsonResponse(
            data=data,
            status=status.HTTP_200_OK,
        )
