from dataclasses import dataclass
from userApp.models import (
    Doctor,
    User,
    DoctorDoctorSpecialization,
    UserPersonalInfo,
    DoctorSummary,
)
from ...serializers.doctor_serializer import DoctorSerializer
from ...serializers.doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from ...serializers.user_personal_info_serializer import UserPersonalInfoSerializer
from ...serializers.doctor_summary_serializer import DoctorSummarySerializer
from ...repositories.doctor_repository import DoctorRepository
from ...repositories.user_repository import UserRepository


@dataclass
class DoctorService:
    doctor_repository: DoctorRepository = DoctorRepository()

    def __get_doctor_info(self, doctor: Doctor):
        user_repository = UserRepository()
        personal_info = self.doctor_repository.get_personal_info_without_fields(
            user_repository, doctor
        )
        specializations = self.doctor_repository.get_doctor_specializations(
            doctor, serialized=True
        )
        summary = self.doctor_repository.get_doctor_summary(doctor, serialized=True)
        return {
            "doctor_slug": doctor.user.slug,
            "personal_info": personal_info,
            "doctor_types": specializations,
            "doctor_summary": summary,
        }

    def get_doctors(self):
        all_doctors = self.doctor_repository.get_all_doctors()
        doctors = [self.__get_doctor_info(doctor) for doctor in all_doctors]
        return {"doctors": doctors}

    def get_doctor(self, slug: str):
        doctor = self.doctor_repository.get_doctor_by(slug=slug)
        return self.__get_doctor_info(doctor)
