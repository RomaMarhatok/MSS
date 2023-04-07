from common.permissions import IsUserAuthenticated
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
)


class ProfileView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = UserService()

    def retrieve(self, request: HttpRequest, user_slug=None):
        return self.service.get_user_info(user_slug, request=request)


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
