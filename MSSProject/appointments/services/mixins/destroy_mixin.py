from django.db import transaction
from django.http import JsonResponse
from rest_framework import exceptions
from ...repositories import AppointmentsRepository


class DestroyAppointmentMixin:
    @transaction.atomic
    def destroy(self, data: dict):
        appointments_repository = AppointmentsRepository()
        doctor_slug = data["doctor_slug"]
        patient_slug = data["patient_slug"]
        date = data["date"]
        if not appointments_repository.is_exist(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        ):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Запись к доктору с такими данными не существует",
                }
            )
        appointments_repository.delete(
            doctor_slug=doctor_slug, patient_slug=patient_slug, date=date
        )
        return JsonResponse(
            data={
                "message": "Запись к доктору удалена",
                "description": "Запись к доктору удалена",
            }
        )
