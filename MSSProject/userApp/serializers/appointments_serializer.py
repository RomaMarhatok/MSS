from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .doctor_serializer import DoctorSerializer
from .patient_serializer import PatientSerializer
from ..models import Appointments, Doctor, Patient
from typing import OrderedDict
from ..utils.date_utils import parse_date_iso_format


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
        kwargs = {
            "doctor": {"validators": []},
            "patient": {"validators": []},
        }

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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["date"] = parse_date_iso_format(rep["date"])
        return rep