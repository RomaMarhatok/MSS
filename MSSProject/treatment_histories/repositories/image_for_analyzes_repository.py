from common.repository.base_repository import AbstractRepository
from ..serializers import ImageForAnlyzeSerializer
from ..models import ImageForAnalyzes


class ImageForAnalyzesRepository(AbstractRepository):
    def get(self, **kwargs):
        super().get(**kwargs)

    def list(self, **kwargs):
        super().list(**kwargs)

    def create(self, data: dict) -> ImageForAnalyzes:
        print(type(data))
        serializer = ImageForAnlyzeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs):
        super().delete(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        super().is_exist(**kwargs)
