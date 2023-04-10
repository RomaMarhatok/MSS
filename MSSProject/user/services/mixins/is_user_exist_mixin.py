from django.http import JsonResponse
from user.repositories import UserRepository
from responses.errors import JsonResponseBadRequest


class IsUserExistMixin:
    def user_exist(self, slug) -> JsonResponse:
        user_repository = UserRepository()
        if not user_repository.is_exist(slug=slug):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидныйе данные в запросе",
                    "description": "Пользователья с таким slug не существует",
                }
            )
        return JsonResponse(data={})
