from rest_framework import status
from django.core.handlers.wsgi import WSGIRequest
from ..models import User
from ..repositories import UserRepository
from ..serializers import (
    UserPersonalInfoSerializer,
    UserLocationSerializer,
    UserSerializer,
)


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

    def create_user(self, data: dict) -> dict:
        # user
        user = data.get("user", None)
        if user is None:
            return {
                "data": {"errors": {"general": ["data about user don't provided"]}},
                "status": status.HTTP_400_BAD_REQUEST,
            }
        user_serializer = UserSerializer(data=user)
        if not user_serializer.is_valid():
            return {"data": {"errors": {user_serializer.errors}}}
        user_serializer.save()

        # user personal info
        user_personal_info = data.get("user_personal_info", None)
        if user_personal_info is None:
            return {
                "data": {
                    "errors": {
                        "general": ["data about user personal info don't provided"]
                    }
                },
                "status": status.HTTP_400_BAD_REQUEST,
            }
        user_personal_info_serializer = UserPersonalInfoSerializer(
            data=user_personal_info, context={"user": user}
        )
        if not user_personal_info_serializer.is_valid():
            return {"data": {"errors": {user_personal_info_serializer.errors}}}
        user_personal_info_serializer.save()

        # user location
        user_location = data.get("user_location", None)
        if user_location is None:
            return {
                "data": {
                    "errors": {"general": ["data about user location don't provided"]}
                },
                "status": status.HTTP_400_BAD_REQUEST,
            }

        user_location_serializer = UserLocationSerializer(
            data=user_location, context={"user": user}
        )
        if user_location_serializer.is_valid():
            return {"data": {"errors": {user_location_serializer.errors}}}
        user_location_serializer.save()
        return {
            "data": {"message": "user was successful registrated"},
            "status": status.HTTP_200_OK,
        }
