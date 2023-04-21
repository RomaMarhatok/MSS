from datetime import datetime
from django.http import JsonResponse
from rest_framework import exceptions
from user.repositories import UserRepository
from user.services.mixins.is_user_exist_mixin import IsUserExistMixin
from ..repositories import AppointmentsRepository
from ..serializers import AppointmentsSerializer
from .mixins.create_mixin import CreateAppointmentMxin
from .mixins.destroy_mixin import DestroyAppointmentMixin


class PatientAppointmentsService(
    CreateAppointmentMxin, DestroyAppointmentMixin, IsUserExistMixin
):
    def __init__(self):
        self.appointments_repository: AppointmentsRepository = AppointmentsRepository()
        self.user_repository: UserRepository = UserRepository()

    def get_patient_appointments(self, patient_slug: str) -> JsonResponse:
        self.is_user_exist(patient_slug)
        appointments_qs = self.appointments_repository.list(
            patient_slug=patient_slug,
        )
        appointments = AppointmentsSerializer(instance=appointments_qs, many=True).data
        return JsonResponse(
            data={"user_appointments": appointments},
        )

    def get_patient_appointment(
        self, patient_slug: str, doctor_slug: str, date: datetime
    ) -> JsonResponse:

        if not self.appointments_repository.is_exist(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        ):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Запись к доктору с такими данными не существует",
                }
            )

        appointment_qs = self.appointments_repository.get(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        )
        appointment = AppointmentsSerializer(instance=appointment_qs).data
        return JsonResponse(data={"appointment": appointment})
