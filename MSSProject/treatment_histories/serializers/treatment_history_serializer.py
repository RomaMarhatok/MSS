from typing import OrderedDict
from rest_framework.serializers import ModelSerializer, SlugField, SerializerMethodField
from ..models import TreatmentHistory


# doctor app imports
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor

# user app imports
from user.models import User


class TreatmentHistorySerializer(ModelSerializer):
    doctor_slug = SlugField(source="doctor.user.slug")
    patient_slug = SlugField(source="patient.slug")
    slug = SerializerMethodField()
    created_at = SerializerMethodField()
    updated_at = SerializerMethodField()

    class Meta:
        model = TreatmentHistory
        fields = (
            "title",
            "short_description",
            "conclusion",
            "description",
            "date",
            "doctor_slug",
            "patient_slug",
            "slug",
            "created_at",
            "updated_at",
        )

    def get_created_at(self, instance: TreatmentHistory):
        return instance.created_at

    def get_updated_at(self, instance: TreatmentHistory):
        return instance.updated_at

    def get_slug(self, instance: TreatmentHistory):
        return instance.slug

    def create(self, validated_data: OrderedDict) -> TreatmentHistory:
        doctor = Doctor.objects.get(user__slug=validated_data["doctor"]["user"]["slug"])
        patient = User.objects.get(slug=validated_data["patient"]["slug"])
        validated_data.pop("doctor")
        validated_data.pop("patient")
        instance = TreatmentHistory.objects.create(
            **validated_data, doctor=doctor, patient=patient
        )
        return instance
