from django.db.models import Q
from .models import User
from common.repository.base_repository import AbstractRepository


class UserRepository(AbstractRepository):
    def __init__(self) -> None:
        self.__init_query = User.objects.select_related(
            "role", "userpersonalinfo", "userlocation"
        )

    def is_exist(self, **kwargs) -> bool:
        login = kwargs.get("login", None)
        password = kwargs.get("password", None)
        if login is not None and password is not None:
            return User.objects.filter(Q(login=login) & Q(password=password)).exists()
        slug = kwargs.get("slug", None)
        if slug is not None:
            return User.objects.filter(slug=slug).exists()
        return False

    def get(self, **kwargs) -> User | None:
        login = kwargs.get("login", None)
        slug = kwargs.get("slug", None)
        try:
            if login is not None:
                return self.__init_query.get(login=login)
            if slug is not None:
                return self.__init_query.get(slug=slug)
            return None
        except User.DoesNotExist:
            return None

    def list(self, **kwargs):
        return super().list(**kwargs)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
