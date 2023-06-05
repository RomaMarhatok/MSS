from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet
from django.http import HttpRequest
from common.permissions import IsUserAuthenticated, IsDoctor
from .services import PatientAppointmentsService, DoctorAppointmentService


class PatientAppointmentsView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = PatientAppointmentsService()

    class CreateInputSerializer(serializers.Serializer):
        doctor_slug = serializers.SlugField()
        patient_slug = serializers.SlugField()
        doctor_specialization_slug = serializers.SlugField()
        date = serializers.DateTimeField()

    class DestroyInputSerializer(serializers.Serializer):
        doctor_slug = serializers.SlugField()
        patient_slug = serializers.SlugField()
        date = serializers.DateTimeField()

    def list(self, request: HttpRequest, patient_slug: str):
        return self.service.get_patient_appointments(patient_slug)

    def retrieve(self, request: HttpRequest, patient_slug=None, doctor_slug=None):
        date = request.data.get("date", None)
        if date is None:
            date = request.GET.get("date", None)
        return self.service.get_patient_appointment(patient_slug, doctor_slug, date)

    def create(self, request: HttpRequest, *args, **kwargs):
        serializer = self.CreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create(serializer.validated_data)

    def destroy(self, request: HttpRequest):
        serializer = self.DestroyInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.destroy(serializer.validated_data)


class DoctorAppointmentsView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = DoctorAppointmentService()

    class CreateInputSerializer(serializers.Serializer):
        doctor_slug = serializers.SlugField()
        patient_slug = serializers.SlugField()
        doctor_specialization_slug = serializers.SlugField()
        date = serializers.DateTimeField()

    class DestroyInputSerializer(serializers.Serializer):
        doctor_slug = serializers.SlugField()
        patient_slug = serializers.SlugField()
        date = serializers.DateTimeField()

    def list(self, request: HttpRequest, doctor_slug: str):
        return self.service.get_doctor_appointments(doctor_slug)

    def retrieve(self, request: HttpRequest, doctor_slug=None, patient_slug=None):
        date = request.data.get("date", None)
        if date is None:
            date = request.GET.get("date", None)
        return self.service.get_doctor_appointment(patient_slug, doctor_slug, date)

    def create(self, request: HttpRequest, *args, **kwargs):
        serializer = self.CreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.create(serializer.validated_data)

    def destroy(self, request: HttpRequest):
        serializer = self.DestroyInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.destroy(serializer.validated_data)
