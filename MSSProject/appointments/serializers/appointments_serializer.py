from rest_framework.serializers import ModelSerializer, SlugField
from datetime import datetime
from typing import OrderedDict
from ..models import Appointments
from common.utils.date_utils import parse_date_to_dict

from user.models import User

from doctor.serializers import DoctorSerializer
from doctor.models import Doctor, DoctorSpecialization


class AppointmentsSerializer(ModelSerializer):
    doctor = DoctorSerializer(required=True)
    patient_slug = SlugField(source="patient.slug")
    doctor_specialization_slug = SlugField(source="doctor_specialization.slug")

    class Meta:
        model = Appointments
        fields = (
            "doctor",
            "patient_slug",
            "doctor_specialization_slug",
            "date",
        )
        extra_kwargs = {
            "doctor": {"validators": []},
        }

    def create(self, validated_data: OrderedDict) -> Appointments:
        doctor = Doctor.objects.get(user__slug=validated_data["doctor"]["user"]["slug"])
        patient = User.objects.get(slug=validated_data["patient"]["slug"])
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
        rep = super().to_representation(instance)
        rep["doctor"] = {"slug": rep["doctor"]["user_slug"]}
        if hasattr(instance.doctor.user, "userpersonalinfo"):
            rep["doctor"]["full_name"] = instance.doctor.user.userpersonalinfo.full_name
        rep["patient"] = {"slug": rep["patient_slug"]}
        if hasattr(instance.patient, "userpersonalinfo"):
            rep["patient"] = instance.patient.userpersonalinfo.full_name
        rep["doctor_specialization"] = {
            "slug": rep["doctor_specialization_slug"],
            "name": instance.doctor_specialization.name,
        }
        rep.pop("doctor_specialization_slug")
        rep.pop("patient_slug")
        rep["parsed_date"] = parse_date_to_dict(rep["date"])
        rep["is_cancelable"] = self.is_cancelable(instance.date)
        return rep

    def is_cancelable(self, appoitment_data: datetime) -> bool:
        d1 = appoitment_data.replace(tzinfo=None)
        d2 = datetime.now().replace(tzinfo=None)
        return (d1 - d2).days > 1
