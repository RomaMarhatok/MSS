from rest_framework import exceptions
from user.repositories import UserRepository


class IsUserExistMixin:
    def is_user_exist(self, slug) -> bool:
        user_repository = UserRepository()
        if not user_repository.is_exist(slug=slug):
            raise exceptions.NotFound(
                detail={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Пользователья с таким slug не существует",
                }
            )
        return True
