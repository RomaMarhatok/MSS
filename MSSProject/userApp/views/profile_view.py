from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse, HttpRequest
from ..permissions.is_user_authenticated import IsUserAuthenticated
from ..services.model_services.user_service import UserService
from rest_framework import status


class ProfileView(GenericViewSet):
    permission_classes = [IsUserAuthenticated]
    lookup_field = "slug"

    def retrieve(self, request: HttpRequest, user_slug=None):
        user_service = UserService()
        serialized_data = user_service.get_user_personal_info(user_slug)
        if serialized_data is not None:
            return JsonResponse(data=serialized_data, status=status.HTTP_200_OK)
        return JsonResponse(
            data={"errors": {"general": ["user don't exist"]}},
            status=status.HTTP_403_FORBIDDEN,
        )
