from pprint import pprint

from common.repository.base_repository import AbstractRepository
from user.serializers import UserPersonalInfoSerializer

from ..models import UserPersonalInfo


class UserPersonalInfoRepository(AbstractRepository):
    def get(self, **kwargs) -> UserPersonalInfo:
        slug = kwargs.get("slug", None)
        if slug is None:
            raise ValueError(
                "class:UserPersonalInfoRepository"
                "function:[GET method]"
                "exception:Argument slug expected"
            )
        return UserPersonalInfo.objects.select_related("user", "user__role").get(
            user__slug=slug
        )

    def list(self, **kwargs):
        return super().list(**kwargs)

    def create(self, data: dict) -> UserPersonalInfo:
        serializer = UserPersonalInfoSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        email = kwargs.get("email", None)
        return UserPersonalInfo.filter(email=email).exists()

    def is_valid(self, data: dict) -> bool:
        serializer = UserPersonalInfoSerializer(data=data)
        return serializer.is_valid(raise_exception=True)
