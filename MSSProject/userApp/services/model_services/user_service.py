from dataclasses import dataclass
from rest_framework import status
from ...repositories.user_repository import UserRepository


@dataclass
class UserService:
    user_repository: UserRepository = UserRepository()

    def get_user_info(self, slug) -> dict | None:
        user = self.user_repository.get_user_by(slug=slug)
        if user is not None:
            user_personal_info = self.user_repository.get_user_personal_info(
                user, serialized=True
            )
            user_location = self.user_repository.get_user_location(
                user, serialized=True
            )
            return {
                "data": {**user_personal_info, **user_location},
                "status": status.HTTP_200_OK,
            }
        return {
            "data": {"errors": {"general": ["user don't exist"]}},
            "status": status.HTTP_403_FORBIDDEN,
        }
