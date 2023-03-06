from dataclasses import dataclass
from rest_framework import status
from ...repositories.appointments_repository import AppointmentsRepository
from ...repositories.user_repository import UserRepository


@dataclass
class AppointmentsService:
    appointments_repository: AppointmentsRepository = AppointmentsRepository()
    user_repository: UserRepository = UserRepository()

    def get_patient_appointments(self, patient_slug: str) -> dict:
        if not self.user_repository.is_user_exist_by_slug(patient_slug):
            return {
                "data": {"errors": {"general": ["patient don't exist"]}},
                "status": status.HTTP_404_NOT_FOUND,
            }
        appointments = self.appointments_repository.get_list_of_appoitments_for_patient(
            patient_slug
        )
        return {
            "data": {"user_appointments": appointments},
            "status": status.HTTP_200_OK,
        }

    def get_doctor_appointments(self, doctor_slug: str) -> dict:
        if not self.user_repository.is_user_exist_by_slug(doctor_slug):
            return {
                "data": {"errors": {"general": ["doctor don't exist"]}},
                "status": status.HTTP_404_NOT_FOUND,
            }
        appointments = self.appointments_repository.get_list_of_appointemnts_for_doctor(
            doctor_slug
        )
        return {
            "data": {"doctor_appointments": appointments},
            "status": status.HTTP_200_OK,
        }

    def get_patient_appointment(self, patient_slug: str, doctor_slug: str) -> dict:
        if patient_slug is None or doctor_slug is None:
            return {
                "data": {"errors": ["data don't provided"]},
                "status": status.HTTP_400_BAD_REQUEST,
            }

        appointment = self.appointments_repository.get_appoitment(
            patient_slug, doctor_slug
        )
        return {"data": appointment, "status": status.HTTP_200_OK}

    def create(self, request_data: dict):
        doctor_slug = request_data["doctor_slug"]
        patient_slug = request_data["patient_slug"]
        doctor_specialization = request_data["doctor_specialization"]
        date = request_data["appointment_date"]
        doctor = self.user_repository.get_user_by(slug=doctor_slug)
        patient = self.user_repository.get_user_by(slug=patient_slug)
        data = {
            # password need only for validators it don't use in create method of serializer
            "doctor": {"user": {"login": doctor.login, "password": doctor.password}},
            "patient": {"user": {"login": patient.login, "password": patient.password}},
            "doctor_specialization": {"slug": doctor_specialization},
            "date": date,
        }
        if self.appointments_repository.is_exist(patient_slug, doctor_slug, date):
            return {
                "data": {"errors": {"general": ["appointments alredy exist"]}},
                "status": status.HTTP_409_CONFLICT,
            }
        appointment, is_created = self.appointments_repository.create_appointment(data)
        if is_created:
            return {
                "data": {
                    "appointment": appointment,
                },
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": appointment},
            "status": status.HTTP_400_BAD_REQUEST,
        }

    def destroy(self, request_data: str):
        doctor_slug = request_data["doctor_slug"]
        patient_slug = request_data["patient_slug"]
        doctor = self.user_repository.get_user_by(slug=doctor_slug)
        patient = self.user_repository.get_user_by(slug=patient_slug)
        count_of_deleted_instantes = self.appointments_repository.delete_appointment(
            doctor, patient
        )
        if isinstance(count_of_deleted_instantes, int):
            return {
                "data": {"message": "appointment was deleted"},
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": ["appointment not exist"]},
            "status": status.HTTP_400_BAD_REQUEST,
        }
