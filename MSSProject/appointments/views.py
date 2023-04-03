from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from common.permissions import IsUserAuthenticated, IsDoctor
from .services.appointments_service import AppointmentsService


class AppointmentsView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def list(self, request: HttpRequest, patient_slug: str):
        appointments_service = AppointmentsService()
        data = appointments_service.get_patient_appointments(patient_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(self, request: HttpRequest, patient_slug=None, doctor_slug=None):
        date = request.data.get("date", None)
        appointments_service = AppointmentsService()
        data = appointments_service.get_patient_appointment(
            patient_slug, doctor_slug, date
        )
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


class DoctorAppointments(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]

    def list(self, request: HttpRequest, doctor_slug: str):
        appointment_service = AppointmentsService()
        data = appointment_service.get_doctor_appointments(doctor_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(
        self,
        request: HttpRequest,
        doctor_slug=None,
        patient_slug=None,
    ):
        date = request.data.get("date", None)
        appointments_service = AppointmentsService()
        data = appointments_service.get_doctor_appointment(
            patient_slug, doctor_slug, date
        )
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )
