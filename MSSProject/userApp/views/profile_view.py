from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from ..services.model_services.user_service import UserService


class ProfileView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def retrieve(self, request: HttpRequest, user_slug=None):
        user_service = UserService()
        serializet_data = user_service.get_user_personal_info(user_slug)
        return JsonResponse(data=serializet_data, status=status.HTTP_200_OK)
