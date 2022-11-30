from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import TreatmentHistory, Doctor, Patient
from .doctor_serializer import DoctorSerializer
from .patient_serializer import PatientSerializer
from .image_for_analyze_serializer import ImageForAnlyzeSerializer


class TreatmentHistorySerializer(ModelSerializer):
    doctor = DoctorSerializer(many=False, required=True)
    patient = PatientSerializer(many=False, required=True)
    image = ImageForAnlyzeSerializer(many=True, required=True)

    class Meta:
        model = TreatmentHistory
        fields = (
            "description",
            "doctor",
            "patient",
        )
        extra_kwargs = {
            "doctor": {"validators": []},
            "patient": {"validators": []},
        }

    def create(self, validated_data: OrderedDict):
        doctor = Doctor.objects.get(
            user__login=validated_data["doctor"]["user"]["login"]
        )
        validated_data.pop("doctor")
        patient = Patient.objects.get(
            user__login=validated_data["doctor"]["user"]["login"]
        )
        validated_data.pop("patient")
        return TreatmentHistory.objects.create(
            **validated_data, doctor=doctor, patient=patient
        )
