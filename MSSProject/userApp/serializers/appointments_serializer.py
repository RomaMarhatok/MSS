from rest_framework.serializers import ModelSerializer
from .doctor_serializer import DoctorSerializer
from .patient_serializer import PatientSerializer
from ..models import Appointments, Doctor, Patient, User
from typing import OrderedDict
from ..utils.date_utils import parse_date_iso_format
from ..repositories.user_repository import UserRepository


class AppointmentsSerializer(ModelSerializer):
    doctor = DoctorSerializer(required=True)
    patient = PatientSerializer(required=True)

    class Meta:
        model = Appointments
        fields = (
            "doctor",
            "patient",
            "date",
        )

    def create(self, validated_data: OrderedDict) -> Appointments:
        doctor = Doctor.objects.get(
            user__login=validated_data["doctor"]["user"]["login"]
        )
        patient = Patient.objects.get(
            user__login=validated_data["patient"]["user"]["login"]
        )
        validated_data.pop("doctor")
        validated_data.pop("patient")
        instance, _ = Appointments.objects.get_or_create(
            **validated_data, doctor=doctor, patient=patient
        )
        return instance

    def to_representation(self, instance: Appointments):
        rep = super().to_representation(instance)
        rep["date"] = parse_date_iso_format(rep["date"])
        rep["doctor"]["user"].pop("login")
        rep["doctor"]["user"].pop("password")
        rep["patient"]["user"].pop("login")
        rep["patient"]["user"].pop("password")
        rep["doctor"]["user"]["full_name"] = self.__get_doctor_full_name(
            instance.doctor.user
        )
        return rep

    def __get_doctor_full_name(self, user: User) -> str:
        user_repository = UserRepository()
        user = user_repository.get_user_by_slug(user.slug)
        return user_repository.get_user_personal_info(user, serialized=True).get(
            "full_name", ""
        )
