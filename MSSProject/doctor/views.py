from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from common.permissions.is_user_authenticated import IsUserAuthenticated
from .services import DoctorService, DoctorSpecializationService
from django.core.handlers.wsgi import WSGIRequest


class DoctorView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: WSGIRequest):
        doctor_service = DoctorService()
        data = doctor_service.get_doctors(request=request)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(self, request: WSGIRequest, doctor_slug: str = None):
        doctor_service = DoctorService()
        data = doctor_service.get_doctor(doctor_slug, request)
        return JsonResponse(data=data["data"], status=data["status"])


class DoctorSpecializationView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest):
        doctor_service = DoctorSpecializationService()
        data = doctor_service.get_doctor_specializations()
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )
