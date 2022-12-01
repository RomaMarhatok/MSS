from rest_framework.viewsets import ViewSet
from .models import Doctor
from .serializers.doctor_serializer import DoctorSerializer
from django.http import JsonResponse
from rest_framework.request import Request


class DoctorViewSet(ViewSet):
    def list(self, request: Request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(instance=doctors, many=True)
        return JsonResponse(serializer.data)
