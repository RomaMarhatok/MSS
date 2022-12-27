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
        user_login = validated_data["doctor"]["user"]["login"]
        doctor = Doctor.objects.filter(user__login=user_login).first()
        validated_data.pop("doctor")
        instance, _ = DoctorSummary.objects.get_or_create(
            **validated_data, doctor=doctor
        )
        return instance
