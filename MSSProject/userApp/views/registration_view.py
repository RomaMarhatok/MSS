from rest_framework.views import APIView
from ..models import Patient, User
from ..serializers.user_serializer import UserSerializer
from ..serializers.user_serializer import UserPersonalInfoSerializer
from django.http import JsonResponse, HttpRequest
from rest_framework.permissions import AllowAny
from ..services.serializer_service import SerializerService
from rest_framework import status


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        print(request.user)
        user_login = request.data["login"]
        if User.is_exist(user_login):
            return JsonResponse(
                data={"errors": {"general": ["user already exist"]}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            print(request.data)
            user_service = SerializerService(UserSerializer, request.data)

            if user_service.errors is not None:
                return JsonResponse(
                    data={"errors": user_service.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

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
                    data={"errors": user_personal_info_service.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return JsonResponse(
                data={"message": "user was successful registrated"},
                status=status.HTTP_200_OK,
            )
