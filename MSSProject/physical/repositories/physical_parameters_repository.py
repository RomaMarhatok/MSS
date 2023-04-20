from common.repository.base_repository import AbstractRepository
from ..models import PhysicalParameters
from ..serializers import PhysicalParametersSerializer


class PhysicalParametersRepository(AbstractRepository):
    def __init__(self) -> None:
        self.qs = PhysicalParameters.objects.select_related(
            "user",
            "user__role",
        )

    def get(self, **kwargs):
        slug = kwargs.get("slug")
        return self.qs.get(slug=slug)

    def list(self, **kwargs):
        patient_slug = kwargs.get("patient_slug")
        return self.qs.filter(user__slug=patient_slug)

    def delete(self, **kwargs):
        slug = kwargs.get("slug")
        return self.qs.filter(slug=slug).delete()

    def create(self, data: dict):
        serializer = PhysicalParametersSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        return super().create(data)

    def update(self, data: dict, instance: PhysicalParameters):
        serializer = PhysicalParametersSerializer(
            instance=instance, data=data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            count_of_updated_rows = serializer.save()
            if count_of_updated_rows == 1:
                return self.get(slug=instance.slug)

    def is_exist(self, **kwargs) -> bool:
        slug = kwargs.get("slug", None)
        return self.qs.filter(slug=slug).exists()
