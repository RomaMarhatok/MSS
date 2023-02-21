from dataclasses import dataclass
from rest_framework import status
from ...repositories.doctor_specialization_repository import (
    DoctorSpecializationRepository,
)
from ...serializers.doctor_specialization_serializer import (
    DoctorSpecializationSerializer,
)


@dataclass
class DoctorTypeService:
    doctor_type_repository: DoctorSpecializationRepository = (
        DoctorSpecializationRepository()
    )

    def get_doctor_types(self):
        instances = self.doctor_type_repository.get_all_doctor_types()
        return {
            "data": {
                "doctor_types": DoctorSpecializationSerializer(
                    instance=instances, many=True
                ).data
            },
            "status": status.HTTP_200_OK,
        }
