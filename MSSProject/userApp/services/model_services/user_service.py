from dataclasses import dataclass
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
            return {**user_personal_info, **user_location}
        return None
