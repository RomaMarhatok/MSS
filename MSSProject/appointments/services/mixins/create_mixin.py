from datetime import datetime
from django.db import transaction
from django.http import JsonResponse
from rest_framework import exceptions
from ...repositories import AppointmentsRepository
from ...serializers import AppointmentsSerializer
from doctor.repositories import DoctorRepository
from doctor.serializers import DoctorSerializer
from user.repositories import UserRepository


class CreateAppointmentMxin:
    @transaction.atomic
    def create(self, data: dict):
        appointment_date: datetime = data.get("date", None)
        if datetime.now().timestamp() > appointment_date.timestamp():
            raise exceptions.ValidationError(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Нельзя создать запись к врачу в прошлом",
                }
            )
        user_repository = UserRepository()
        patient_slug = data.get("patient_slug", None)
        if not user_repository.is_exist(slug=patient_slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Пользватель с таким slug не существует",
                },
            )

        doctor_repository = DoctorRepository()
        doctor_slug = data.get("doctor_slug", None)
        if not doctor_repository.is_exist(slug=doctor_slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Доктора с таким slug не существует",
                },
            )
        doctor = doctor_repository.get(slug=doctor_slug)
        data["doctor"] = DoctorSerializer(instance=doctor).data

        appointments_repository = AppointmentsRepository()

        appointment = appointments_repository.create(data)
        serialized_appointment = AppointmentsSerializer(instance=appointment).data
        return JsonResponse(
            data={
                "appointment": serialized_appointment,
            }
        )
