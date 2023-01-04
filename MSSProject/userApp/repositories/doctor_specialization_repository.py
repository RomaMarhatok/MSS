from django.db.models import QuerySet
from ..models import DoctorSpecialization


class DoctorSpecializationRepository:
    def get_all_doctor_types(self) -> QuerySet[DoctorSpecialization]:
        return DoctorSpecialization.objects.all()
