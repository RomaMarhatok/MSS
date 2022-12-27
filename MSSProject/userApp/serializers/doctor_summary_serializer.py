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
        user_slug = validated_data["doctor"]["user"]["slug"]
        doctor = Doctor.objects.filter(user__slug=user_slug).first()
        validated_data.pop("doctor")
        instance, _ = DoctorSummary.objects.create(**validated_data, doctor=doctor)
        return instance
