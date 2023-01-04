from django.db.models import Q
from dataclasses import dataclass
from .mapper.mapper import Mapper
from rest_framework.authtoken.models import Token
from ..models import User, UserPersonalInfo, UserLocation
from ..serializers.user_personal_info_serializer import UserPersonalInfoSerializer
from ..serializers.user_location_serializer import UserLocationSerializer


@dataclass
class UserRepository:
    function_mapper: Mapper = Mapper()

    def is_user_exist(self, login, password) -> bool:
        return User.objects.filter(Q(login=login) & Q(password=password)).exists()

    def get_user_by(self, **kwargs) -> User:
        function_map = {
            ("token",): self.get_user_by_token,
            ("login",): self.get_user_by_login,
            ("slug",): self.get_user_by_slug,
        }
        return self.function_mapper.mapping(function_map, kwargs=kwargs)

    def get_user_by_token(self, token_key: str) -> User | None:
        return Token.objects.filter(key=token_key).first().user

    def get_user_by_login(self, login: str) -> User | None:
        return (
            User.objects.filter(login=login)
            .select_related("role", "userpersonalinfo", "userlocation")
            .first()
        )

    def get_user_by_slug(self, slug) -> User | None:
        user = (
            User.objects.filter(slug=slug)
            .select_related("role", "userpersonalinfo", "userlocation")
            .first()
        )
        return user

    def get_user_personal_info(
        self, user: User, not_necessary_fields=None, serialized=False
    ) -> UserPersonalInfo | dict:
        instance = user.userpersonalinfo
        serialized_data = UserPersonalInfoSerializer(
            instance=instance, context={"not_necessary_fields": not_necessary_fields}
        ).data
        return serialized_data if serialized else instance

    def get_user_location(self, user: User, serialized=False) -> UserLocation | dict:
        instance = user.userlocation
        serialized_data = UserLocationSerializer(instance=instance).data
        return serialized_data if serialized else instance
