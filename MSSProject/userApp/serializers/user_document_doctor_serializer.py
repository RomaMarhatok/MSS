from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from .user_serializer import UserDocumentSerializer
from .doctor_serializer import DoctorSerializer
from ..models import UserDocumentDoctor, Doctor, UserDocument


class UserDocumentDoctorSerializer(ModelSerializer):
    user_document = UserDocumentSerializer(many=False, required=False)
    doctor = DoctorSerializer(many=False, required=False)

    class Meta:
        model = UserDocumentDoctor
        fields = (
            "user_document",
            "doctor",
        )

    def create(self, validated_data):
        user_document = UserDocument.objects.get(
            user__slug=validated_data["user_document"]["user"]["slug"]
        )
        doctor = Doctor.objects.get(user__slug=validated_data["doctor"]["slug"])
        instance, _ = UserDocumentDoctor.objects.get_or_create(
            doctor=doctor, user_document=user_document
        )
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return {
            "user_document_slug": rep["user_document"]["slug"],
            "doctor_slug": rep["doctor"]["user"]["slug"],
            "document_typr": rep["user_document"]["document_type"],
        }
