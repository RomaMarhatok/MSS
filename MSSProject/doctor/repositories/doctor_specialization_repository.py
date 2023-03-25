from django.db.models import QuerySet
from ..models import DoctorSpecialization
from common.repository.base_repository import AbstractRepository


class DoctorSpecializationRepository(AbstractRepository):
    def list(self, **kwargs) -> QuerySet[DoctorSpecialization]:
        return DoctorSpecialization.objects.all()

    def get(self, **kwargs) -> DoctorSpecialization | None:
        slug = kwargs.get("slug", None)
        if slug is None:
            return None
        try:
            return DoctorSpecialization.objects.get(slug=slug)
        except DoctorSpecialization.DoesNotExist:
            return None
        except DoctorSpecialization.MultipleObjectsReturned:
            return None

    def is_exist(self, **kwargs) -> bool:
        return super().is_exist(**kwargs)

    def create(self, data: dict):
        return super().create(data)

    def delete(self, **kwargs):
        return super().delete(**kwargs)
