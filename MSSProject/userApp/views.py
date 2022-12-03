from rest_framework.viewsets import ViewSet
from .models import Doctor, Patient
from .serializers.doctor_serializer import DoctorSerializer
from .serializers.patient_serializer import PatientSerializer
from django.http import JsonResponse
from rest_framework.request import Request


class DoctorViewSet(ViewSet):
    lookup_field = "slug"
    queryset = Doctor.objects.all()

    def list(self, request: Request):
        serializer = DoctorSerializer(instance=self.queryset, many=True)
        return JsonResponse(data=serializer.data)

    def retrieve(self, request: Request, slug=None):
        doctor = self.queryset.get(slug=slug)
        serializer = DoctorSerializer(instance=doctor)
        return JsonResponse(data=serializer.data)


class PatientViewSet(ViewSet):
    lookup_field = "slug"
    queryset = Patient.objects.all()

    def list(self, request: Request):
        serializer = PatientSerializer(instance=self.queryset, many=True)
        return JsonResponse(data=serializer.data)

    def retrieve(self, request: Request, slug=None):
        patient = self.queryset.get(slug=slug)
        serializer = PatientSerializer(instance=patient)
        return JsonResponse(data=serializer.data)
