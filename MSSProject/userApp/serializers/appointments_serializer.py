# buildin
from typing import OrderedDict

# serializers
from .doctor_serializer import DoctorSerializer
from .patient_serializer import PatientSerializer
from .doctor_specialization_serializer import DoctorSpecializationSerializer
from rest_framework.serializers import ModelSerializer
from .user_personal_info_serializer import UserPersonalInfoSerializer

# utils
from ..utils.date_utils import parse_date_iso_format
from datetime import datetime

# models
from ..models import Appointments, Doctor, Patient, User, DoctorSpecialization


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
        extra_kwargs = {
            "doctor": {"validators": []},
            "patient": {"validators": []},
            "doctor_specialization": {"validators": []},
        }

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
        rep = None
        if "is_doctor" in self.context and self.context["is_doctor"]:
            rep = self.doctor_representation(instance)
        else:
            rep = self.patient_representation(instance)
        rep["is_cancelable"] = self.is_cancelable(instance.date)
        return rep

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

    def is_cancelable(self, appoitment_data: datetime) -> bool:
        d1 = appoitment_data.replace(tzinfo=None)
        d2 = datetime.now().replace(tzinfo=None)
        return (d1 - d2).days > 1

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
        personal_info = UserPersonalInfoSerializer(instance=user.userpersonalinfo).data
        return (
            personal_info.get("first_name", "")
            + " "
            + personal_info.get("second_name", "")
            + " "
            + personal_info.get("patronymic", "")
        )
