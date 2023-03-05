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

    def get_doctor_specializations(self):
        instances = self.doctor_type_repository.get_doctor_specializations()
        serializer = DoctorSpecializationSerializer(instance=instances, many=True)
        return {
            "data": {"doctor_types": serializer.data},
            "status": status.HTTP_200_OK,
        }

    def get_doctor_specialization(self, doctor_specialization_slug: str):
        instance = self.doctor_type_repository.get_doctor_specialization(
            doctor_specialization_slug
        )
        serializer = DoctorSpecializationSerializer(instance=instance)
        return {"data": {"doctor_type": serializer.data}, "status": status.HTTP_200_OK}
