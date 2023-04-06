from common.repository.base_repository import AbstractRepository
from user.serializers import UserLocationSerializer

from ..models import UserLocation


class UserLocationRepository(AbstractRepository):
    def get(self, **kwargs) -> UserLocation:
        slug = kwargs.get("slug", None)
        if slug is None:
            raise ValueError(
                "class:UserLocationRepository"
                "function:[GET method]"
                "exception:argument slug"
            )
        return UserLocation.objects.select_related("user", "user__role").get(
            user__slug=slug
        )

    def list(self, **kwargs):
        return super().list(**kwargs)

    def create(self, data: dict) -> UserLocation:
        serializer = UserLocationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def is_exist(self, **kwargs) -> bool:
        return super().is_exist(**kwargs)

    def delete(self, **kwargs):
        return super().delete(**kwargs)

    def is_valid(self, data: dict) -> bool:
        serializer = UserLocationSerializer(data=data)
        return serializer.is_valid(raise_exception=True)
