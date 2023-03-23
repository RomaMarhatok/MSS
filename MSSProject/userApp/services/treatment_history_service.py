from rest_framework import status
from ..repositories import TreatmentHistoryRepository
from ..repositories import UserRepository
from ..serializers import TreatmentHistorySerializer, UserPersonalInfoSerializer
from django.http import HttpRequest


class TreatmentHistoryService:
    def __init__(self) -> None:
        self.treatment_repository: TreatmentHistoryRepository = (
            TreatmentHistoryRepository()
        )
        self.user_repository: UserRepository = UserRepository()

    def get_patient_treatment_histories(
        self, patient_slug: str, doctor_specialization_slug: str, request=None
    ):
        if self.user_repository.is_exist(slug=patient_slug):
            treatments_histories = self.treatment_repository.list(
                patient_slug=patient_slug,
                doctor_specialization_slug=doctor_specialization_slug,
            )
            user = self.user_repository.get(slug=patient_slug)
            user_personal_info = UserPersonalInfoSerializer(
                instance=user.userpersonalinfo, context={"request": request}
            ).data
            return {
                "data": {
                    "patient_info": user_personal_info,
                    "treatment_histories": TreatmentHistorySerializer(
                        instance=treatments_histories, many=True
                    ).data,
                },
                "status": status.HTTP_200_OK,
            }
        return {"data": ["patient don't exist"], "status": status.HTTP_404_NOT_FOUND}

    def get_treatment_history(self, patient_slug: str, treatment_history_slug):
        if self.user_repository.is_exist(slug=patient_slug):
            if self.treatment_repository.is_exist(
                treatment_history_slug=treatment_history_slug
            ):
                treatment = self.treatment_repository.get(
                    patient_slug=patient_slug,
                    treatment_history_slug=treatment_history_slug,
                )

                return {
                    "data": TreatmentHistorySerializer(
                        instance=treatment,
                    ).data,
                    "status": status.HTTP_200_OK,
                }
            return {
                "data": {"errors": ["treatment history don't exist"]},
                "status": status.HTTP_404_NOT_FOUND,
            }
        return {
            "data": {"errors": ["patient don't exist"]},
            "status": status.HTTP_404_NOT_FOUND,
        }

    def create_treatment_history(self, request: HttpRequest):
        treatment_history = self.treatment_repository.create(request.data)
        serializer = TreatmentHistorySerializer(instance=treatment_history)
        if treatment_history is not None:
            return {
                "data": serializer.data,
                "status": status.HTTP_400_BAD_REQUEST,
            }
        return {
            "data": {"errors": []},
            "status": status.HTTP_200_OK,
        }
