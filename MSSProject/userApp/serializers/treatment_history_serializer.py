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
            "description",
            "doctor",
            "patient",
            "slug",
        )
        extra_kwargs = {
            "doctor": {"validators": []},
            "patient": {"validators": []},
            "slug": {"required": False},
            "url": {"lookup_field": "slug"},
        }

    def create(self, validated_data: OrderedDict) -> TreatmentHistory:
        doctor = Doctor.objects.get(
            user__login=validated_data["doctor"]["user"]["login"]
        )
        patient = Patient.objects.get(
            user__login=validated_data["patient"]["user"]["login"]
        )
        instance, _ = TreatmentHistory.objects.get_or_create(
            description=validated_data["description"], doctor=doctor, patient=patient
        )
        return instance
