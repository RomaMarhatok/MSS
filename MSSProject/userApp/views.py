from rest_framework.viewsets import ViewSet
from .models import Doctor
from .serializers.doctor_serializer import DoctorSerializer
from django.http import JsonResponse
from rest_framework.request import Request


class DoctorViewSet(ViewSet):
    lookup_field = "slug"
    queryset = Doctor.objects.all()

    def list(self, request: Request):
        serializer = DoctorSerializer(instance=self.queryset, many=True)
        return JsonResponse(serializer.data)

    def retrieve(self, request, slug=None):
        doctor = self.queryset.get(slug=slug)
        serializer = DoctorSerializer(instance=doctor)
        return JsonResponse(serializer.data)
