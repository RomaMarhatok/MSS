from rest_framework.views import APIView
from django.http import JsonResponse, HttpRequest
from rest_framework.permissions import AllowAny
from ..services.authentication_service import AuthenticationService


class AuthenticationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: HttpRequest):
        service = AuthenticationService(request)
        authentication_info = service.authenticate_user()
        return JsonResponse(
            data=authentication_info["data"], status=authentication_info["status"]
        )
