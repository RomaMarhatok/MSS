from userApp.models import Doctor, User, DoctorDoctorSpecialization, UserPersonalInfo
from ...serializers.doctor_serializer import DoctorSerializer
from ...serializers.doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)
from ...serializers.user_personal_info_serializer import UserPersonalInfoSerializer


class DoctorService:
    def get_doctor_by_slug(self, slug):
        doctor = Doctor.objects.filter(user__slug=slug).first()
        return self.get_serializet_doctor(doctor)

    def get_serializet_doctor(self, doctor):
        doctor_data = DoctorSerializer(instance=doctor).data
        user_personal_info = self.get_user_personal_info(doctor.user)
        doctor_specializations = self.get_doctor_specializations(doctor)
        return {
            "doctor_slug": doctor_data["user"]["slug"],
            "personal_info": user_personal_info,
            "doctor_types": doctor_specializations,
        }

    def get_doctor_specializations(self, doctor: Doctor):
        doctor_specialization = [
            DoctorSpecializationSerializer(
                instance=doctor_specialization.doctor_specialization
            ).data
            for doctor_specialization in DoctorDoctorSpecialization.objects.filter(
                doctor__user__pk=doctor.user.pk
            )
        ]
        return doctor_specialization

    def get_user_personal_info(self, user: User):
        user_personal_info = UserPersonalInfo.objects.filter(user=user).first()
        user_personal_info_data = UserPersonalInfoSerializer(
            instance=user_personal_info
        ).data
        not_neccessary_data = (
            "gender",
            "email",
            "health_status",
        )
        for key in not_neccessary_data:
            user_personal_info_data.pop(key)
        full_name = (
            user_personal_info.first_name
            + " "
            + user_personal_info.second_name
            + " "
            + user_personal_info.patronymic
        )
        user_personal_info_data.update({"full_name": full_name})
        return user_personal_info_data

    def get_all_doctors(self):
        all_doctors = Doctor.objects.all()
        doctors = [self.get_serializet_doctor(doctor) for doctor in all_doctors]
        return {"doctors": doctors}
