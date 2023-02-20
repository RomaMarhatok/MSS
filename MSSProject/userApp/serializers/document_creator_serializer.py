from rest_framework.serializers import ModelSerializer
from .document_serializer import DocumentSerializer
from .doctor_serializer import DoctorSerializer
from ..models import DocumentCreator, Doctor, Document


class DocumentCreatorSerializer(ModelSerializer):
    document = DocumentSerializer(many=False, required=False)
    creator = DoctorSerializer(many=False, required=False)

    class Meta:
        model = DocumentCreator
        fields = (
            "document",
            "creator",
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

    def to_representation(self, instance: DocumentCreator):
        document_serializer_context = {}
        if "include_context" in self.context:
            document_serializer_context.update(
                {"include_context": self.context["include_context"]}
            )
        serialized_document = DocumentSerializer(
            instance=instance.document,
            context=document_serializer_context,
        ).data
        serialized_document.update({"creator": {"slug": instance.creator.user.slug}})
        rep = serialized_document
        return rep
