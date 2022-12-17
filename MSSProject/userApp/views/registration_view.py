from rest_framework.views import APIView
from django.http import JsonResponse, HttpRequest
from rest_framework.permissions import AllowAny
from ..services.registration_service import RegistrationService


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        registration_service = RegistrationService(request)
        registration_info = registration_service.register_user()
        return JsonResponse(
            data=registration_info["data"], status=registration_info["status"]
        )
