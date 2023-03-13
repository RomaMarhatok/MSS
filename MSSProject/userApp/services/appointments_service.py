from dataclasses import dataclass
from rest_framework import status
from ..repositories import AppointmentsRepository, UserRepository
from ..serializers import AppointmentsSerializer
from datetime import datetime


@dataclass
class AppointmentsService:
    def __init__(self):
        self.appointments_repository: AppointmentsRepository = AppointmentsRepository()
        self.user_repository: UserRepository = UserRepository()

    def get_patient_appointments(self, patient_slug: str) -> dict:
        if not self.user_repository.is_exist(slug=patient_slug):
            return {
                "data": {"errors": {"general": ["patient don't exist"]}},
                "status": status.HTTP_404_NOT_FOUND,
            }
        appointments = self.appointments_repository.list(
            patient_slug=patient_slug,
        )
        serialized_appointments = AppointmentsSerializer(
            instance=appointments, many=True
        ).data
        return {
            "data": {"user_appointments": serialized_appointments},
            "status": status.HTTP_200_OK,
        }

    def get_doctor_appointments(self, doctor_slug: str) -> dict:
        if not self.user_repository.is_exist(slug=doctor_slug):
            return {
                "data": {"errors": {"general": ["doctor don't exist"]}},
                "status": status.HTTP_404_NOT_FOUND,
            }
        appointments = self.appointments_repository.list(doctor_slug=doctor_slug)
        serialized_appointments = AppointmentsSerializer(
            instance=appointments, many=True, context={"is_doctor": True}
        ).data
        return {
            "data": {"doctor_appointments": serialized_appointments},
            "status": status.HTTP_200_OK,
        }

    def get_doctor_appointment(
        self, patient_slug: str, doctor_slug: str, date: datetime
    ) -> dict:
        if not self.user_repository.is_exist(slug=doctor_slug):
            return {
                "data": {"errors": {"general": ["doctor don't exist"]}},
                "status": status.HTTP_404_NOT_FOUND,
            }
        if self.appointments_repository.is_exist(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        ):
            appointments = self.appointments_repository.get(
                patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
            )
            serialized_appointment = AppointmentsSerializer(
                instance=appointments, context={"is_doctor": True}
            ).data
            return {
                "data": serialized_appointment,
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": {"general": ["appointents don't exist"]}},
            "status": status.HTTP_200_OK,
        }

    def get_patient_appointment(
        self, patient_slug: str, doctor_slug: str, date: datetime
    ) -> dict:

        if patient_slug is None or doctor_slug is None or date is None:
            return {
                "data": {"errors": ["data don't provided"]},
                "status": status.HTTP_400_BAD_REQUEST,
            }
        appointment = self.appointments_repository.get(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        )
        serialized_appointment = AppointmentsSerializer(instance=appointment).data
        return {"data": serialized_appointment, "status": status.HTTP_200_OK}

    def create(self, request_data: dict):
        doctor_slug = request_data["doctor_slug"]
        patient_slug = request_data["patient_slug"]
        doctor_specialization = request_data["doctor_specialization"]
        date = request_data["appointment_date"]
        if not self.user_repository.is_exist(slug=patient_slug):
            return {
                "data": {"errors": {"general": ["patient don't exist"]}},
                "status": status.HTTP_409_CONFLICT,
            }
        if not self.user_repository.is_exist(slug=doctor_slug):
            return {
                "data": {"errors": {"general": ["doctor don't exist"]}},
                "status": status.HTTP_409_CONFLICT,
            }
        doctor = self.user_repository.get(slug=doctor_slug)
        patient = self.user_repository.get(slug=patient_slug)
        data = {
            # password need only for validators it don't use in create method of serializer
            "doctor": {"user": {"login": doctor.login, "password": doctor.password}},
            "patient": {"user": {"login": patient.login, "password": patient.password}},
            "doctor_specialization": {"slug": doctor_specialization},
            "date": date,
        }
        if self.appointments_repository.is_exist(
            patient_slug=patient_slug, doctor_slug=doctor_slug, date=date
        ):
            return {
                "data": {"errors": {"general": ["appointments alredy exist"]}},
                "status": status.HTTP_409_CONFLICT,
            }

        is_created, appointment = self.appointments_repository.create(data)
        if is_created:
            serialized_appointment = AppointmentsSerializer(instance=appointment).data
            return {
                "data": {
                    "appointment": serialized_appointment,
                },
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": appointment},
            "status": status.HTTP_400_BAD_REQUEST,
        }

    def destroy(self, request_data: dict):
        doctor_slug = request_data["doctor_slug"]
        patient_slug = request_data["patient_slug"]
        date = request_data["date"]
        count_of_deleted_instantes = self.appointments_repository.delete(
            doctor_slug=doctor_slug, patient_slug=patient_slug, date=date
        )
        if count_of_deleted_instantes > 0:
            return {
                "data": {"message": "appointment was deleted"},
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": ["appointment not exist"]},
            "status": status.HTTP_400_BAD_REQUEST,
        }
