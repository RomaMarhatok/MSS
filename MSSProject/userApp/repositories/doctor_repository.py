from .mapper.mapper import Mapper
from dataclasses import dataclass
from .user_repository import UserRepository
from ..models import Doctor, DoctorSummary, DoctorDoctorSpecialization
from ..serializers.doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from ..serializers.doctor_summary_serializer import DoctorSummarySerializer


@dataclass
class DoctorRepository:

    function_mapper: Mapper = Mapper()

    def get_doctor_by(self, **kwargs) -> Doctor:
        function_map = {("slug",): self.get_doctor_by_slug}
        return self.function_mapper.mapping(function_map, kwargs=kwargs)

    def get_doctor_by_slug(self, slug) -> Doctor:
        return Doctor.objects.filter(user__slug=slug).first()

    def get_doctor_summary(self, doctor, serialized=False) -> DoctorSummary | dict:
        summary_instance = DoctorSummary.objects.filter(doctor=doctor).first()
        summary_serialized = DoctorSummarySerializer(instance=summary_instance).data
        return summary_serialized if serialized else summary_instance

    def get_all_doctors(self):
        return Doctor.objects.all()

    def get_full_doctor_personal_info(
        self, user_repository: UserRepository, doctor: Doctor
    ):
        return user_repository.get_user_personal_info(doctor.user, serialized=True)

    def get_personal_info_without_fields(
        self,
        user_repository: UserRepository,
        doctor: Doctor,
    ):
        return user_repository.get_user_personal_info(
            doctor.user,
            not_necessary_fields=[
                "gender",
                "email",
                "health_status",
            ],
            serialized=True,
        )

    def get_doctor_specializations(self, doctor: Doctor, serialized=False):
        doctor_specialization_instances = [
            doctor_doctor_specialization.doctor_specialization
            for doctor_doctor_specialization in DoctorDoctorSpecialization.objects.filter(
                doctor=doctor
            )
        ]
        doctor_specialization_serialized = DoctorSpecializationSerializer(
            instance=doctor_specialization_instances, many=True
        ).data

        return (
            doctor_specialization_serialized
            if serialized
            else doctor_specialization_instances
        )
