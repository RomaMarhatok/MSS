from typing import OrderedDict
from rest_framework.serializers import ModelSerializer, SlugField, SerializerMethodField
from ..models import TreatmentHistory
from common.utils.date_utils import parse_date_to_dict

# doctor app imports
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
        extra_kwargs = {"short_description": {"allow_blank": True}}

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

    def update(self, instance: TreatmentHistory, validated_data) -> int:
        return TreatmentHistory.objects.filter(slug=instance.slug).update(
            **validated_data
        )
        # return super().update(instance, validated_data)

    def to_representation(self, instance: TreatmentHistory):
        rep = super().to_representation(instance)
        rep["parsed_date"] = parse_date_to_dict(rep["date"])
        rep["doctor"] = {
            "slug": instance.doctor.user.slug,
        }
        if hasattr(instance.doctor.user, "userpersonalinfo"):
            rep["doctor"]["full_name"] = instance.doctor.user.userpersonalinfo.full_name
        rep["string_date"] = (
            str(rep["parsed_date"]["hours"])
            + ":"
            + str(rep["parsed_date"]["minutes"])
            + " "
            + str(rep["parsed_date"]["day"])
            + " "
            + str(rep["parsed_date"]["mounth"])
            + " "
            + str(rep["parsed_date"]["year"])
        )
        return rep
