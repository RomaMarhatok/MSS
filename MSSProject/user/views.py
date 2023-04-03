from rest_framework.viewsets import GenericViewSet
from common.permissions import IsUserAuthenticated
from django.http import HttpRequest, JsonResponse
from .services import (
    UserService,
    AuthenticationService,
    RegistrationService,
    LogOutService,
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status


class ProfileView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"
    service = UserService()

    def retrieve(self, request: HttpRequest, user_slug=None):
        response_data = self.service.get_user_info(user_slug, request=request)
        return JsonResponse(data=response_data["data"], status=response_data["status"])


class AuthenticationView(APIView):
    permission_classes = [AllowAny]
    service = AuthenticationService()

    def post(self, request: HttpRequest):
        authentication_info = self.service.authenticate(request)
        return JsonResponse(
            data=authentication_info["data"], status=authentication_info["status"]
        )


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        registration_service = RegistrationService()
        registration_info = registration_service.registrate(request)
        return JsonResponse(
            data=registration_info["data"], status=registration_info["status"]
        )


class LogOutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_slug: str = None):
        log_out_service = LogOutService()
        log_out_service.logout(user_slug)
        return JsonResponse(data={}, status=status.HTTP_200_OK)
