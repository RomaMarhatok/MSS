from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ...permissions.is_user_authenticated import IsUserAuthenticated
from ...services.model_services.appointments_service import AppointmentsService


class AppointmentsView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest, patient_slug: str):
        appointments_service = AppointmentsService()
        data = appointments_service.get_all(patient_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(self, request: HttpRequest, patient_slug=None, doctor_slug=None):
        appointments_service = AppointmentsService()
        data = appointments_service.get(patient_slug, doctor_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def create(self, request: HttpRequest, *args, **kwargs):
        appointments_service = AppointmentsService()
        data = appointments_service.create(request.data)
        return JsonResponse(data=data["data"], status=data["status"])

    def destroy(self, request: HttpRequest):
        appointments_service = AppointmentsService()
        data = appointments_service.destroy(request.data)
        return JsonResponse(data=data["data"], status=data["status"])
