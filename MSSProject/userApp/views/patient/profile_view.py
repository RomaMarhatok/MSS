from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ...permissions.is_user_authenticated import IsUserAuthenticated
from ...services.user_service import UserService
from rest_framework import status


class ProfileView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def retrieve(self, request: HttpRequest, user_slug=None):
        user_service = UserService()
        response_data = user_service.get_user_info(user_slug, request=request)
        return JsonResponse(data=response_data["data"], status=response_data["status"])
