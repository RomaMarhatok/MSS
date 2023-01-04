from dataclasses import dataclass
from userApp.models import Doctor
from ...repositories.user_repository import UserRepository
from ...repositories.doctor_repository import DoctorRepository


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
