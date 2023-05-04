from rest_framework import serializers
from common.repository.base_repository import AbstractRepository
from user.serializers import UserLocationSerializer

from ..models import UserLocation


class UserLocationRepository(AbstractRepository):
    class SlugSerializer(serializers.Serializer):
        slug = serializers.SlugField()

    def _validation_kwargs(self, kwargs):
        slug_serialzer = self.SlugSerializer(data=kwargs)
        if slug_serialzer.is_valid():
            return slug_serialzer.validated_data
        raise ValueError(
            f"class:{self.__class__}"
            "function:[_validate_kwargs method]"
            "exception: Any kwargs arguments expected"
        )

    def get(self, **kwargs) -> UserLocation:
        data = self._validation_kwargs(kwargs)
        return UserLocation.objects.select_related("user", "user__role").get(**data)

    def list(self, **kwargs):
        return UserLocation.objects.all()

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
