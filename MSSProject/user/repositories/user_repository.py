from common.repository.base_repository import AbstractRepository
from user.serializers import UserSerializer

from ..models import User


class UserRepository(AbstractRepository):
    def is_exist(self, **kwargs) -> bool:
        login = kwargs.get("login", None)
        if login is not None:
            return User.objects.filter(login=login).exists()
        slug = kwargs.get("slug", None)
        if slug is not None:
            return User.objects.filter(slug=slug).exists()
        return False

    def get(self, **kwargs) -> User:

        qs = User.objects.select_related("role", "userpersonalinfo", "userlocation")

        login = kwargs.get("login", None)
        if login is not None:
            return qs.get(login=login)

        slug = kwargs.get("slug", None)
        if slug is not None:
            return qs.get(slug=slug)

    def list(self, **kwargs):
        return super().list(**kwargs)

    def create(self, data: dict) -> User:
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_valid(self, data: dict) -> bool:
        serializer = UserSerializer(data=data)
        return serializer.is_valid(raise_exception=True)
