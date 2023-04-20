from rest_framework import exceptions
from user.repositories import UserRepository
from responses.errors import JsonResponseBadRequest


class IsUserExistMixin:
    def is_user_exist(self, slug) -> bool:
        user_repository = UserRepository()
        if not user_repository.is_exist(slug=slug):
            raise exceptions.ValidationError(
                detail={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Пользователья с таким slug не существует",
                }
            )
        return True
