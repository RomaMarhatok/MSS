from django.db.models import QuerySet
from ..models import DoctorSpecialization


class DoctorSpecializationRepository:
    def get_doctor_specializations(self) -> QuerySet[DoctorSpecialization]:
        return DoctorSpecialization.objects.all()

    def get_doctor_specialization(
        self, doctor_specialization_slug: str
    ) -> QuerySet[DoctorSpecialization]:
        return DoctorSpecialization.objects.filter(slug=doctor_specialization_slug)
