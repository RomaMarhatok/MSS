from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from .models import Doctor, Patient, User
from .serializers.doctor_serializer import DoctorSerializer
from .serializers.user_serializer import UserSerializer
from .serializers.patient_serializer import PatientSerializer
from .serializers.user_serializer import UserPersonalInfoSerializer
from django.http import JsonResponse, HttpRequest
from rest_framework.authtoken.models import Token
from django.db.models import QuerySet
from rest_framework.permissions import AllowAny
from .services.serializer_service import SerializerService


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
        user_login = request.data["login"]
        if User.is_exist(user_login):
            return JsonResponse(
                data={"errors": {"general": ["user already exist"]}}, status=400
            )
        else:
            print(request.data)
            user_service = SerializerService(UserSerializer, request.data)

            if user_service.errors is not None:
                return JsonResponse(data={"errors": user_service.errors}, status=400)

            Patient.objects.create(user=user_service.serialize_instance)

            user_personal_info_service = SerializerService(
                UserPersonalInfoSerializer,
                {
                    "user": {"login": user_login, "password": request.data["password"]},
                    "first_name": request.data["first_name"],
                    "second_name": request.data["second_name"],
                },
            )
            if user_personal_info_service.errors is not None:
                return JsonResponse(
                    data={"errors": user_personal_info_service.errors}, status=400
                )
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
