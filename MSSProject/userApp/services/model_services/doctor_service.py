from .user_service import UserService
from userApp.models import Doctor
from ...serializers.doctor_serializer import DoctorSerializer


class DoctorService(UserService):
    def get_doctor_by_slug(self, slug):
        doctor = Doctor.objects.filter(user__slug=slug).first()
        data = DoctorSerializer(instance=doctor).data
        return data

    def get_doctor_types(self, doctor: Doctor):
        return DoctorSerializer(instance=doctor).data["doctor_types"]

    def get_all_doctors(self):
        all_doctors = Doctor.objects.all()
        serializer = DoctorSerializer(instance=all_doctors, many=True)
        return {"doctors": serializer.data}
