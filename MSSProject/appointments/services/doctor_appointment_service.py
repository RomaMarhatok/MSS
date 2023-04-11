from datetime import datetime
from django.http import JsonResponse

from responses.errors import JsonResponseBadRequest
from user.repositories import UserRepository
from user.services.mixins.is_user_exist_mixin import IsUserExistMixin

from ..repositories import AppointmentsRepository
from ..serializers import AppointmentsSerializer
from .mixins.create_mixin import CreateAppointmentMxin
from .mixins.destroy_mixin import DestroyAppointmentMixin


class DoctorAppointmentService(
    CreateAppointmentMxin, DestroyAppointmentMixin, IsUserExistMixin
):
    def __init__(self):
        self.appointments_repository: AppointmentsRepository = AppointmentsRepository()
        self.user_repository: UserRepository = UserRepository()

    def get_doctor_appointments(self, doctor_slug: str) -> JsonResponse:
        response = self.user_exist(doctor_slug)
        if response.status_code == 400:
            return response
        appointments_qs = self.appointments_repository.list(doctor_slug=doctor_slug)
        appointments = AppointmentsSerializer(instance=appointments_qs, many=True).data
        return JsonResponse(
            data={
                "doctor_appointments": appointments,
            }
        )

    def get_doctor_appointment(
        self, patient_slug: str, doctor_slug: str, date: datetime
    ) -> JsonResponse:
        if not self.appointments_repository.is_exist(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Запись к доктору с такими данными не существует",
                }
            )
        appointment_qs = self.appointments_repository.get(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        )
        appointment = AppointmentsSerializer(instance=appointment_qs).data
        return JsonResponse(data={"appointment": appointment})
