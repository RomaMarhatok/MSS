from rest_framework import serializers
from common.repository.base_repository import AbstractRepository
from user.serializers import UserPersonalInfoSerializer

from ..models import UserPersonalInfo


class UserPersonalInfoRepository(AbstractRepository):
    class SlugSerializer(serializers.Serializer):
        slug = serializers.SlugField()

    class EmailSerialzier(serializers.Serializer):
        email = serializers.EmailField()

    def _validate_kwargs(self, kwargs) -> dict:
        slug_serializer = self.SlugSerializer(data=kwargs)
        if slug_serializer.is_valid():
            return slug_serializer.validated_data
        email_serialzer = self.EmailSerialzier(data=kwargs)
        if email_serialzer.is_valid():
            return email_serialzer.validated_data
        raise ValueError(
            f"class:{self.__class__}"
            "function:[_validate_kwargs method]"
            "exception: Any kwargs arguments expected"
        )

    def get(self, **kwargs) -> UserPersonalInfo:
        slug = kwargs.get("slug", None)
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
        data = self._validate_kwargs(kwargs)
        return UserPersonalInfo.objects.filter(**data).exists()

    def is_valid(self, data: dict) -> bool:
        serializer = UserPersonalInfoSerializer(data=data)
        return serializer.is_valid(raise_exception=True)
