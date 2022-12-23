from rest_framework.serializers import ModelSerializer
from .user_serializer import UserDocumentSerializer
from .doctor_serializer import DoctorSerializer
from ..models import DocumentCreator, Doctor, Document


class UserDocumentDoctorSerializer(ModelSerializer):
    user_document = UserDocumentSerializer(many=False, required=False)
    doctor = DoctorSerializer(many=False, required=False)

    class Meta:
        model = DocumentCreator
        fields = (
            "user_document",
            "doctor",
        )

    def create(self, validated_data):
        user_document = Document.objects.get(
            user__slug=validated_data["user_document"]["user"]["slug"]
        )
        doctor = Doctor.objects.get(user__slug=validated_data["doctor"]["slug"])
        instance, _ = DocumentCreator.objects.get_or_create(
            doctor=doctor, user_document=user_document
        )
        return instance
