from rest_framework.views import APIView
from rest_framework import status
from userApp.services.log_out_service import LogOutService
from django.http import JsonResponse


class LogOutView(APIView):
    def get(self, request, format=None, user_slug: str = None):
        log_out_service = LogOutService()
        log_out_service.logout(user_slug)
        return JsonResponse(data={}, status=status.HTTP_200_OK)
