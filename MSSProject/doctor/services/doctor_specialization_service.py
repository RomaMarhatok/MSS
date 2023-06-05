from django.http import JsonResponse
from ..repositories import (
    DoctorSpecializationRepository,
)
from ..serializers import (
    DoctorSpecializationSerializer,
)


class DoctorSpecializationService:
    def __init__(self) -> None:
        self.doctor_type_repository: DoctorSpecializationRepository = (
            DoctorSpecializationRepository()
        )

    def get_doctor_specializations(self):
        data = DoctorSpecializationSerializer(
            instance=self.doctor_type_repository.list(), many=True
        ).data
        return JsonResponse(data={"doctor_types": data})

    def get_doctor_specialization(self, doctor_specialization_slug: str):
        data = DoctorSpecializationSerializer(
            instance=self.doctor_type_repository.get(slug=doctor_specialization_slug)
        ).data
        return JsonResponse(data={"doctor_type": data})
