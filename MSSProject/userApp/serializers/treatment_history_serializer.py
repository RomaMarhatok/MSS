from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import TreatmentHistory, Doctor, Patient
from .doctor_serializer import DoctorSerializer
from .patient_serializer import PatientSerializer


class TreatmentHistorySerializer(ModelSerializer):
    doctor = DoctorSerializer(many=False, required=True)
    patient = PatientSerializer(many=False, required=True)

    class Meta:
        model = TreatmentHistory
        fields = (
            "title",
            "short_description",
            "conclusion",
            "description",
            "date",
            "doctor",
            "patient",
            "slug",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "doctor": {"validators": []},
            "patient": {"validators": []},
            "slug": {"required": False},
            "url": {"lookup_field": "slug"},
            "created_at": {"required": False},
            "updated_at": {"required": False},
        }

    def create(self, validated_data: OrderedDict) -> TreatmentHistory:
        doctor = Doctor.objects.get(user__slug=validated_data["doctor"]["user"]["slug"])
        patient = Patient.objects.get(
            user__slug=validated_data["patient"]["user"]["slug"]
        )
        validated_data.pop("doctor")
        validated_data.pop("patient")
        instance, _ = TreatmentHistory.objects.get_or_create(
            **validated_data, doctor=doctor, patient=patient
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("doctor")
        rep["patient_slug"] = rep["patient"]["user"]["slug"]
        rep.pop("patient")
        return rep
