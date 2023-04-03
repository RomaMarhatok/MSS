from typing import OrderedDict
from rest_framework.serializers import ModelSerializer
from ..models import TreatmentHistory


# doctor app imports
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor

# user app imports
from user.serializers import UserSerializer
from user.models import User


class TreatmentHistorySerializer(ModelSerializer):
    doctor = DoctorSerializer(many=False, required=True)
    patient = UserSerializer(many=False, required=True)

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
        doctor = Doctor.objects.get(
            user__login=validated_data["doctor"]["user"]["login"]
        )
        patient = User.objects.get(login=validated_data["patient"]["login"])
        validated_data.pop("doctor")
        validated_data.pop("patient")
        instance, _ = TreatmentHistory.objects.get_or_create(
            **validated_data, doctor=doctor, patient=patient
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("doctor")
        rep["patient_slug"] = rep["patient"]["slug"]
        rep.pop("patient")
        return rep
