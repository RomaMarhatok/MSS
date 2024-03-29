from django.http import HttpRequest
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from common.permissions.is_doctor import IsDoctor
from common.permissions.is_user_authenticated import IsUserAuthenticated
from .services import DoctorTreatmentHistoryService, PatientTreatmentHistoryService


class UserTreatmentHistoriesView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    service = PatientTreatmentHistoryService()

    def list(self, request: HttpRequest, patient_slug: str):
        return self.service.get_user_treatments_histories_list(patient_slug, request)

    def retrieve(self, request: HttpRequest, treatment_slug: str):
        return self.service.get_user_treatments_history(treatment_slug, request)


# doctor views
class PatientTreatmentsView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DoctorTreatmentHistoryService()

    def list(
        self, request: HttpRequest, patient_slug: str, doctor_specialization_slug: str
    ):
        return self.service.get_patient_treatment_histories_list(
            patient_slug,
            doctor_specialization_slug=doctor_specialization_slug,
            request=request,
        )

    def retrieve(self, request: HttpRequest, treatment_slug: str):
        return self.service.get_patient_treatment_history(treatment_slug, request)


class CreateTreatmentHistoryView(APIView):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DoctorTreatmentHistoryService()

    class InputSerializer(serializers.Serializer):
        date = serializers.DateTimeField()
        patient_slug = serializers.SlugField()
        doctor_slug = serializers.SlugField()
        title = serializers.CharField()
        short_description = serializers.CharField(allow_blank=True)
        description = serializers.CharField()
        conclusion = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_treatment_history(serializer.validated_data)


class UpdateTreatmentHistoryView(APIView):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DoctorTreatmentHistoryService()

    class InputSerializer(serializers.Serializer):
        treatment_history_slug = serializers.SlugField()
        title = serializers.CharField()
        short_description = serializers.CharField()
        description = serializers.CharField()
        conclusion = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.update_treatment_history(serializer.validated_data)


class CreateImageForAnalyzesView(APIView):
    permission_classes = [IsUserAuthenticated, IsDoctor]

    service = DoctorTreatmentHistoryService()
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    class InputSerializer(serializers.Serializer):
        treatment_history_slug = serializers.SlugField()
        description = serializers.CharField()
        image = serializers.ImageField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_image_for_analyzes(
            serializer.validated_data, request=request
        )


class DeleteImageForAnalyzesView(APIView):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DoctorTreatmentHistoryService()

    class InputSerializer(serializers.Serializer):
        treatment_history_slug = serializers.SlugField()
        image_for_analyzes_slug = serializers.SlugField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.delete_image_for_analyzes(serializer.validated_data)


class DocumentTreatmentHistoryView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DoctorTreatmentHistoryService()

    class CreateInputSerializer(serializers.Serializer):
        treatment_history_slug = serializers.SlugField()
        document_slug = serializers.SlugField()

    def create(self, request):
        serializer = self.CreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.add_document_to_treatment_history(
            **serializer.validated_data
        )

    class DeleteInputSerializer(serializers.Serializer):
        treatment_history_slug = serializers.SlugField()
        document_slug = serializers.SlugField()

    def delete(self, request):
        serializer = self.DeleteInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.delete_document_from_treatment_history(
            **serializer.validated_data
        )
