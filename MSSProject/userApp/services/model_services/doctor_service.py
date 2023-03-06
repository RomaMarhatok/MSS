from dataclasses import dataclass
from rest_framework import status
from userApp.models import Doctor
from ...repositories.user_repository import UserRepository
from ...repositories.doctor_repository import DoctorRepository


@dataclass
class DoctorService:
    doctor_repository: DoctorRepository = DoctorRepository()
    user_repository: UserRepository = UserRepository()

    def __get_doctor_info(self, doctor: Doctor):
        personal_info = self.doctor_repository.get_personal_info_without_fields(
            self.user_repository, doctor
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
        return {"data": {"doctors": doctors}, "status": status.HTTP_200_OK}

    def is_exist(self, slug: str) -> bool:
        if self.user_repository.is_user_exist_by_slug(slug):
            user = self.user_repository.get_user_by_slug(slug)
            if user.role.name == "doctor":
                return True
        return False

    def get_doctor(self, slug: str):
        if self.is_exist(slug):
            doctor = self.doctor_repository.get_doctor_by(slug=slug)
            return {
                "data": self.__get_doctor_info(doctor),
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": ["doctor don't exist"]},
            "status": status.HTTP_404_NOT_FOUND,
        }
