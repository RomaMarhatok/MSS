from django.http import JsonResponse
from rest_framework import exceptions
from ..serializers import (
    DoctorSpecializationSerializer,
    DoctorSummarySerializer,
)
from ..models import Doctor, DoctorSummary
from ..repositories import DoctorRepository


class DoctorService:
    def __init__(self):
        self.doctor_repository: DoctorRepository = DoctorRepository()

    def _get_response_data(self, doctor: Doctor):
        doctor_slug = doctor.user.slug
        try:
            doctor_summary = DoctorSummarySerializer(instance=doctor.doctorsummary).data
        except DoctorSummary.DoesNotExist:
            doctor_summary = {}
        ds = [
            DoctorSpecializationSerializer(
                instance=doctor_doctor_specialization.doctor_specialization
            ).data
            for doctor_doctor_specialization in doctor.doctor_doctor_specialization.all()
        ]
        if not hasattr(doctor.user, "userpersonalinfo"):
            return {
                "doctor_slug": doctor_slug,
                "doctor_summary": doctor_summary,
                "doctor_types": ds,
            }
        full_name = doctor.user.userpersonalinfo.full_name
        return {
            "doctor_slug": doctor_slug,
            "doctor_full_name": full_name,
            "doctor_summary": doctor_summary,
            "doctor_types": ds,
        }

    def get_doctors(self):
        doctors = [
            self._get_response_data(doctor) for doctor in self.doctor_repository.list()
        ]
        return JsonResponse(data={"doctors": doctors})

    def get_doctor(self, slug: str):
        if not self.doctor_repository.is_exist(slug=slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": "Доктора с таким slug не существует",
                },
            )
        doctor = self.doctor_repository.get(slug=slug)
        return JsonResponse(data={"doctors": self._get_response_data(doctor)})
