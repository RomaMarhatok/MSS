# buildin
from typing import OrderedDict

# serializers
from .doctor_serializer import DoctorSerializer
from .patient_serializer import PatientSerializer
from .doctor_specialization_serializer import DoctorSpecializationSerializer
from rest_framework.serializers import ModelSerializer

# utils
from ..utils.date_utils import parse_date_iso_format

# models
from ..models import Appointments, Doctor, Patient, User, DoctorSpecialization

# repositories
from ..repositories.user_repository import UserRepository


class AppointmentsSerializer(ModelSerializer):
    doctor = DoctorSerializer(required=True)
    patient = PatientSerializer(required=True)
    doctor_specialization = DoctorSpecializationSerializer(required=True)

    class Meta:
        model = Appointments
        fields = (
            "doctor",
            "patient",
            "doctor_specialization",
            "date",
        )

    def create(self, validated_data: OrderedDict) -> Appointments:
        doctor = Doctor.objects.get(
            user__login=validated_data["doctor"]["user"]["login"]
        )
        patient = Patient.objects.get(
            user__login=validated_data["patient"]["user"]["login"]
        )
        doctor_specialization = DoctorSpecialization.objects.get(
            slug=validated_data["doctor_specialization"]["slug"]
        )
        validated_data.pop("doctor")
        validated_data.pop("patient")
        validated_data.pop("doctor_specialization")
        instance, _ = Appointments.objects.get_or_create(
            **validated_data,
            doctor=doctor,
            patient=patient,
            doctor_specialization=doctor_specialization
        )
        return instance

    def to_representation(self, instance: Appointments):
        if "is_doctor" in self.context and self.context["is_doctor"]:
            return self.doctor_representation(instance)
        return self.patient_representation(instance)

    def patient_representation(self, instance: Appointments):
        rep = super().to_representation(instance)
        rep["date"] = parse_date_iso_format(rep["date"])
        rep["doctor"]["user"].pop("login")
        rep["doctor"]["user"].pop("password")
        rep.pop("patient")
        rep["doctor"]["user"]["full_name"] = self.__get_user_full_name(
            instance.doctor.user
        )
        return rep

    def doctor_representation(self, instance: Appointments):
        rep = super().to_representation(instance)
        rep["date"] = parse_date_iso_format(rep["date"])
        slug = rep["patient"]["user"]["slug"]
        rep["patient"]["user"] = {
            "full_name": self.__get_user_full_name(instance.patient.user),
            "slug": slug,
        }
        rep.pop("doctor")
        return rep

    def __get_user_full_name(self, user: User) -> str:
        user_repository = UserRepository()
        user = user_repository.get_user_by_slug(user.slug)
        return user_repository.get_user_personal_info(user, serialized=True).get(
            "full_name", ""
        )
