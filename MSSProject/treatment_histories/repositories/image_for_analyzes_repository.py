from common.repository.base_repository import AbstractRepository
from ..serializers import ImageForAnlyzeSerializer
from ..models import ImageForAnalyzes


class ImageForAnalyzesRepository(AbstractRepository):
    def get(self, **kwargs) -> ImageForAnalyzes:
        slug = kwargs.get("slug", None)
        return ImageForAnalyzes.objects.get(slug=slug)

    def list(self, **kwargs):
        treatment_history = kwargs.get("treatment_history", None)
        return ImageForAnalyzes.objects.filter(
            treatment_history_image_for_analyzes__treatment_history=treatment_history
        )

    def create(self, data: dict) -> ImageForAnalyzes:
        serializer = ImageForAnlyzeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs):
        super().delete(**kwargs)

    def is_exist(self, **kwargs) -> bool:
        super().is_exist(**kwargs)
