from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from .models import Doctor, Patient, User
from .serializers.doctor_serializer import DoctorSerializer
from .serializers.user_serializer import UserSerializer
from .serializers.patient_serializer import PatientSerializer
from django.http import JsonResponse, HttpRequest
from rest_framework.authtoken.models import Token
from django.db.models import QuerySet
from rest_framework.permissions import AllowAny


class DoctorViewSet(ViewSet):
    lookup_field = "slug"
    queryset = Doctor.objects.all()

    def list(self, request: HttpRequest):
        serializer = DoctorSerializer(instance=self.queryset, many=True)
        return JsonResponse(data=serializer.data)

    def retrieve(self, request: HttpRequest, slug=None):
        doctor = self.queryset.get(slug=slug)
        serializer = DoctorSerializer(instance=doctor)
        return JsonResponse(data=serializer.data)


class PatientViewSet(ViewSet):
    lookup_field = "slug"
    queryset = Patient.objects.all()

    def list(self, request: HttpRequest):
        serializer = PatientSerializer(instance=self.queryset, many=True)
        return JsonResponse(data=serializer.data)

    def retrieve(self, request: HttpRequest, slug=None):
        patient = self.queryset.get(slug=slug)
        serializer = PatientSerializer(instance=patient)
        return JsonResponse(data=serializer.data)


class TokenRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        users: QuerySet = User.objects.filter(
            login=request.data["login"], password=request.data["password"]
        )
        if users.exists():
            return JsonResponse(data={"errors": ["user already exist"]}, status=400)
        else:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return JsonResponse(data={"errors": serializer.errors}, status=400)
            user = serializer.save()
            Token.objects.create(user=user)
            Patient.objects.create(user=user)
            return JsonResponse(
                data={"message": "user was successful registrated"}, status=200
            )


class TokenAuthenticationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        users: QuerySet = User.objects.filter(
            login=request.data["login"], password=request.data["password"]
        )
        if users.exists():
            user = users.first()
            user_auth_token_key = Token.objects.filter(user=user).first().key
            return JsonResponse(
                data={
                    "message": "user successful authenticated",
                    "token": user_auth_token_key,
                    "user_role": user.role.name,
                },
                status=200,
            )
        return JsonResponse(data={"errors": "user don't exist"}, status=400)
