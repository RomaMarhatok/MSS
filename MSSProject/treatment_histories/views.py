from django.http import HttpRequest
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from .services.treatment_history_service import TreatmentHistoryService
from common.permissions.is_doctor import IsDoctor
from common.permissions.is_user_authenticated import IsUserAuthenticated


class PatientTreatmentsView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = TreatmentHistoryService()

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
    service = TreatmentHistoryService()

    class InputSerializer(serializers.Serializer):
        date = serializers.DateTimeField()
        patient_slug = serializers.CharField()
        doctor_slug = serializers.CharField()
        title = serializers.CharField()
        short_description = serializers.CharField()
        description = serializers.CharField()
        conclusion = serializers.CharField()
        doctor_slug = serializers.CharField()
        patient_slug = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_treatment_history(serializer.validated_data)


class UserTreatmentHistoriesView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    service = TreatmentHistoryService()
    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def list(self, request: HttpRequest, patient_slug: str):
        return self.service.get_user_treatments_histories_list(patient_slug, request)

    def retrieve(self, request: HttpRequest, treatment_slug: str):
        return self.service.get_user_treatments_history(treatment_slug, request)


class CreateImageForAnalyzesView(APIView):
    service = TreatmentHistoryService()

    class InputSerializer(serializers.Serializer):
        treatment_history_slug = serializers.SlugField()
        description = serializers.CharField()
        image = serializers.ImageField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create_image_for_analyzes(serializer.validated_data)
