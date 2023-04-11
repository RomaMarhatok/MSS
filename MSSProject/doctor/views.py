from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from common.permissions.is_user_authenticated import IsUserAuthenticated
from .services import DoctorService, DoctorSpecializationService
from django.core.handlers.wsgi import WSGIRequest


class DoctorView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = DoctorService()

    def list(self, request: HttpRequest):
        return self.service.get_doctors()

    def retrieve(self, request: HttpRequest, doctor_slug: str = None):
        return self.service.get_doctor(doctor_slug)


class DoctorSpecializationView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = DoctorSpecializationService()

    def list(self, request: HttpRequest):
        return self.service.get_doctor_specializations()
