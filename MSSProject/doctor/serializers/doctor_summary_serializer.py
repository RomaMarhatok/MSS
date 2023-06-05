from rest_framework.serializers import ModelSerializer
from ..models import DoctorSummary, Doctor
from .doctor_serializer import DoctorSerializer


class DoctorSummarySerializer(ModelSerializer):
    doctor = DoctorSerializer(required=True)

    class Meta:
        model = DoctorSummary
        fields = (
            "doctor",
            "short_summary",
            "summary",
        )

    def create(self, validated_data):
        doctor = Doctor.objects.filter(
            user__slug=validated_data["doctor"]["user"]["slug"]
        ).first()
        validated_data.pop("doctor")
        instance, _ = DoctorSummary.objects.get_or_create(
            **validated_data, doctor=doctor
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("doctor")
        return rep
