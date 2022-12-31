from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from ..services.model_services.doctor_service import DoctorService


class DoctorView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest):
        doctor_service = DoctorService()
        data = doctor_service.get_doctors()
        return JsonResponse(
            data=data,
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request: HttpRequest, doctor_slug: str = None):
        doctor_service = DoctorService()
        data = doctor_service.get_doctor(doctor_slug)
        return JsonResponse(data=data, status=status.HTTP_200_OK)
