from .mapper.mapper import Mapper
from dataclasses import dataclass
from .user_repository import UserRepository
from ..models import Doctor, DoctorSummary, DoctorDoctorSpecialization
from ..serializers.doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from ..serializers.doctor_summary_serializer import DoctorSummarySerializer
from django.db.models import QuerySet, Prefetch
from django.core.handlers.wsgi import WSGIRequest


@dataclass
class DoctorRepository:

    function_mapper: Mapper = Mapper()

    def get_doctor_by(self, **kwargs) -> Doctor:
        function_map = {("slug",): self.get_doctor_by_slug}
        return (
            self.function_mapper.mapping(function_map, kwargs=kwargs)
            .prefetch_related(
                Prefetch(
                    "doctor_doctor_specialization",
                    queryset=DoctorDoctorSpecialization.objects.select_related(
                        "doctor_specialization"
                    ).all(),
                )
            )
            .select_related(
                "user",
                "user__role",
                "user__userpersonalinfo",
                "user__userlocation",
                "doctorsummary",
            )
            .first()
        )

    def get_doctor_by_slug(self, slug) -> QuerySet[Doctor]:
        return Doctor.objects.filter(user__slug=slug)

    def get_doctors_by_specialization(
        self, doctor_specialization_slug: str
    ) -> QuerySet[tuple[str]]:
        return DoctorDoctorSpecialization.objects.filter(
            doctor_specialization__slug=doctor_specialization_slug
        ).values_list("doctor__user__slug")

    def get_doctor_summary(self, doctor, serialized=False) -> DoctorSummary | dict:
        summary_serialized = DoctorSummarySerializer(instance=doctor.doctorsummary).data
        return summary_serialized if serialized else doctor.doctorsummary

    def get_all_doctors(self) -> QuerySet[Doctor]:
        return (
            Doctor.objects.prefetch_related(
                Prefetch(
                    "doctor_doctor_specialization",
                    queryset=DoctorDoctorSpecialization.objects.select_related(
                        "doctor_specialization"
                    ).all(),
                )
            )
            .select_related(
                "user",
                "user__role",
                "user__userpersonalinfo",
                "user__userlocation",
                "doctorsummary",
            )
            .all()
        )

    def get_full_doctor_personal_info(
        self, user_repository: UserRepository, doctor: Doctor
    ):
        return user_repository.get_user_personal_info(doctor.user, serialized=True)

    def get_personal_info_without_fields(
        self,
        user_repository: UserRepository,
        doctor: Doctor,
        request: WSGIRequest = None,
    ):
        return user_repository.get_user_personal_info(
            doctor.user,
            not_necessary_fields=[
                "gender",
                "email",
                "health_status",
            ],
            serialized=True,
            request=request,
        )

    def get_doctor_specializations(self, doctor: Doctor, serialized=False):
        doctor_doctor_specialization_queryset = (
            doctor.doctor_doctor_specialization.all()
        )
        doctor_specialization_instances = [
            doctor_doctor_specialization.doctor_specialization
            for doctor_doctor_specialization in doctor_doctor_specialization_queryset
        ]
        doctor_specialization_serialized = DoctorSpecializationSerializer(
            instance=doctor_specialization_instances, many=True
        ).data

        return (
            doctor_specialization_serialized
            if serialized
            else doctor_specialization_instances
        )
