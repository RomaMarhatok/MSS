from common.permissions import IsUserAuthenticated, IsDoctor
from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import serializers
from .services import (
    AuthenticationService,
    LogOutService,
    RegistrationService,
    UserService,
    VerificationService,
    EmailService,
)


class PatientView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]
    service = UserService()

    def list(self, request):
        return self.service.get_all_patients()


class ProfileView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = UserService()

    def retrieve(self, request: HttpRequest, user_slug=None):
        return self.service.get_user_info(user_slug, request=request)

    class UpdateInputSerializer(serializers.Serializer):
        user_slug = serializers.SlugField()
        first_name = serializers.CharField()
        second_name = serializers.CharField()
        patronymic = serializers.CharField()
        email = serializers.CharField()
        gender = serializers.CharField()
        age = serializers.IntegerField()
        health_status = serializers.CharField()

    def update(self, request: HttpRequest):
        serializer = self.UpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.update_user_info(serializer.validated_data)


class AuthenticationView(APIView):
    permission_classes = [AllowAny]
    service = AuthenticationService()

    class InputSerializer(serializers.Serializer):
        login = serializers.CharField()
        password = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.authenticate(serializer.validated_data)


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    service = RegistrationService()

    class InputSerializer(serializers.Serializer):
        login = serializers.CharField()
        password = serializers.CharField()
        first_name = serializers.CharField()
        second_name = serializers.CharField()
        patronymic = serializers.CharField()
        email = serializers.CharField()
        gender = serializers.CharField()
        age = serializers.IntegerField()
        address = serializers.CharField()
        country = serializers.CharField()
        city = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.registrate(serializer.data)


class LogOutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_slug: str = None):
        log_out_service = LogOutService()
        log_out_service.logout(user_slug)
        return JsonResponse(data={}, status=status.HTTP_200_OK)


class UserValidationView(APIView):
    service = UserService()

    class InputSerializer(serializers.Serializer):
        login = serializers.CharField()
        password = serializers.CharField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.validate_user(serializer.validated_data)


class UserPersonalInfoValidationView(APIView):
    service = UserService()

    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        second_name = serializers.CharField()
        patronymic = serializers.CharField()
        email = serializers.CharField()
        gender = serializers.CharField()
        age = serializers.IntegerField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.validate_personal_info(serializer.validated_data)


class CitiesView(APIView):
    permission_classes = [AllowAny]
    service = UserService()

    def get(self, request: HttpRequest):
        return self.service.get_cities()


class VerifyAccountView(APIView):
    permission_classes = [AllowAny]
    service = VerificationService()

    def get(self, request: HttpRequest, uid, token):
        return self.service.verify(uid, token)


class SendEmailView(APIView):
    permission_classes = [AllowAny]
    service = EmailService()

    class InputSerializer(serializers.Serializer):
        link = serializers.CharField()
        email = serializers.EmailField()

    def post(self, request: HttpRequest):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.service.send_verification_email(serializer.validated_data)
