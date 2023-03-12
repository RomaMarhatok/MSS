from rest_framework import status
from django.core.handlers.wsgi import WSGIRequest
from ..repositories import UserRepository
from ..serializers import UserPersonalInfoSerializer, UserLocationSerializer


class UserService:
    def __init__(self) -> None:
        self.user_repository: UserRepository = UserRepository()

    def get_user_info(self, slug, request: WSGIRequest) -> dict | None:
        user = self.user_repository.get(slug=slug)
        if user is not None:
            user_personal_info = UserPersonalInfoSerializer(
                instance=user.userpersonalinfo, context={"request": request}
            ).data
            user_location = UserLocationSerializer(
                instance=user.userlocation,
            ).data
            return {
                "data": {**user_personal_info, **user_location},
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": {"general": ["user don't exist"]}},
            "status": status.HTTP_403_FORBIDDEN,
        }
