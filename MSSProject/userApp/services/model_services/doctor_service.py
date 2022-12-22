from .user_service import UserService
from userApp.models import Doctor
from userApp.serializers.doctor_serializer import DoctorSerializer


class DoctorService(UserService):
    def get_doctor_info(self, slug):
        user_personal_info = self.get_user_personal_info(slug)
        doctor = Doctor.objects.filter(user__slug=slug).first()
        doctor_types = self.get_doctor_types(doctor)
        return {
            "first_name": user_personal_info["first_name"],
            "second_name": user_personal_info["second_name"],
            "patronymic": user_personal_info["patronymic"],
            "doctor_types": doctor_types,
        }

    def get_doctor_types(self, doctor: Doctor):
        return DoctorSerializer(instance=doctor).data["doctor_types"]

    def get_all_doctors(self):
        all_doctors = Doctor.objects.all()
        serializer = DoctorSerializer(instance=all_doctors, many=True)
        return {"doctors": serializer.data}
