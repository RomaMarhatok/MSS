from dataclasses import dataclass
from rest_framework import status
from userApp.models import (
    DoctorDoctorSpecialization,
    DoctorSummary,
    UserPersonalInfo,
    Doctor,
)
from ..repositories import DoctorRepository
from ..serializers import (
    DoctorSpecializationSerializer,
    DoctorSummarySerializer,
    UserPersonalInfoSerializer,
)

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet


class DoctorService:
    def __init__(self):
        self.doctor_repository: DoctorRepository = DoctorRepository()

    def __get_doctor_info(
        self,
        doctor: Doctor,
        doctor_doctor_specialozations: QuerySet[DoctorDoctorSpecialization],
        request: WSGIRequest = None,
    ):
        specializations = self.__get_doctor_specializations(
            doctor_doctor_specialozations
        )
        summary = self.__get_doctor_summary(doctor)
        personal_info = self.__get_doctor_personal_info(doctor, request=request)
        return {
            "doctor_slug": doctor.user.slug,
            "personal_info": personal_info,
            "doctor_types": specializations,
            "doctor_summary": summary,
        }

    def get_doctors(self, request: WSGIRequest = None):
        doctors = [
            self.__get_doctor_info(doctor, doctor_specializations, request=request)
            for (doctor, doctor_specializations) in self.doctor_repository.list()
        ]
        return {"data": {"doctors": doctors}, "status": status.HTTP_200_OK}

    def get_doctor(self, slug: str, request: WSGIRequest = None):
        if self.doctor_repository.is_exist(slug=slug):
            doctor, doctor_doctor_specialozations = self.doctor_repository.get(
                slug=slug
            )
            return {
                "data": self.__get_doctor_info(
                    doctor, doctor_doctor_specialozations, request=request
                ),
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": ["doctor don't exist"]},
            "status": status.HTTP_404_NOT_FOUND,
        }

    def __get_doctor_specializations(
        self, doctor_doctor_specialozations: QuerySet[DoctorDoctorSpecialization]
    ):
        specializations = [
            doctor_doctor_specialozation.doctor_specialization
            for doctor_doctor_specialozation in doctor_doctor_specialozations
        ]
        serialized_specializations = DoctorSpecializationSerializer(
            instance=specializations, many=True
        ).data
        return serialized_specializations

    def __get_doctor_summary(self, doctor: Doctor) -> dict:
        try:
            return DoctorSummarySerializer(instance=doctor.doctorsummary).data
        except DoctorSummary.DoesNotExist:
            return {}

    def __get_doctor_personal_info(
        self,
        doctor: Doctor,
        request: WSGIRequest = None,
    ) -> dict:
        try:
            not_necessary_fields = [
                "gender",
                "email",
                "health_status",
            ]
            return UserPersonalInfoSerializer(
                instance=doctor.user.userpersonalinfo,
                context={
                    "not_necessary_fields": not_necessary_fields,
                    "request": request,
                },
            ).data
        except UserPersonalInfo.DoesNotExist:
            return {}
