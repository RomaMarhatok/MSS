from django.http import JsonResponse, HttpRequest
from rest_framework.viewsets import GenericViewSet
from userApp.permissions.is_doctor import IsDoctor
from userApp.permissions.is_user_authenticated import IsUserAuthenticated
from userApp.services.model_services.appointments_service import AppointmentsService


class DoctorAppointments(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]

    def list(self, request: HttpRequest, doctor_slug: str):
        appointment_service = AppointmentsService()
        data = appointment_service.get_doctor_appointments(doctor_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(self, request: HttpRequest, patient_slug=None, doctor_slug=None):
        appointments_service = AppointmentsService()
        data = appointments_service.get_patient_appointment(patient_slug, doctor_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )
