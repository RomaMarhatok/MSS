from django.db.models import Q
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.authtoken.models import Token
from ..models import User, UserPersonalInfo, UserLocation
from ..serializers.user_personal_info_serializer import UserPersonalInfoSerializer
from ..serializers.user_location_serializer import UserLocationSerializer
from .base import AbstractRepository


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

    # def is_user_exist(self, login, password) -> bool:
    #     return (
    #         User.objects.filter(Q(login=login) & Q(password=password)).exists()
    #         or User.objects.filter(Q(login=login) & Q(username=login)).exists()
    #     )

    # def is_user_exist_by_slug(self, slug) -> bool:
    #     return User.objects.filter(slug=slug).exists()

    # def get_user_by(self, **kwargs) -> User | None:
    #     function_map = {
    #         ("login",): self.get_user_by_login,
    #         ("slug",): self.get_user_by_slug,
    #     }
    #     return self.function_mapper.mapping(function_map, kwargs=kwargs)

    # def get_user_by_login(self, login: str) -> User | None:
    #     return (
    #         User.objects.filter(login=login)
    #         .select_related("role", "userpersonalinfo", "userlocation")
    #         .first()
    #     )

    # def get_user_by_slug(self, slug) -> User | None:
    #     user = (
    #         User.objects.filter(slug=slug)
    #         .select_related("role", "userpersonalinfo", "userlocation")
    #         .first()
    #     )
    #     return user

    # def get_user_personal_info(
    #     self,
    #     user: User,
    #     not_necessary_fields=None,
    #     serialized=False,
    #     request: WSGIRequest = None,
    # ) -> UserPersonalInfo | dict:
    #     try:
    #         instance = user.userpersonalinfo
    #     except UserPersonalInfo.DoesNotExist:
    #         return {}
    #     serialized_data = UserPersonalInfoSerializer(
    #         instance=instance,
    #         context={"not_necessary_fields": not_necessary_fields, "request": request},
    #     ).data
    #     return serialized_data if serialized else instance

    # def get_user_location(self, user: User, serialized=False) -> UserLocation | dict:
    #     instance = user.userlocation
    #     serialized_data = UserLocationSerializer(instance=instance).data
    #     return serialized_data if serialized else instance
