from django.http import JsonResponse, HttpRequest
from rest_framework import exceptions
from user.repositories import UserRepository, UserPersonalInfoRepository
from ...models import TreatmentHistory
from ...repositories import (
    TreatmentHistoryRepository,
    ImageForAnalyzesRepository,
    TreatmentHistoryImageForAnalyzesRepository,
)
from ...serializers import TreatmentHistorySerializer, ImageForAnlyzeSerializer

from user.services.mixins.is_user_exist_mixin import IsUserExistMixin


class BaseTreatmentHistoryService(IsUserExistMixin):
    def __init__(self) -> None:
        self.treatment_history_repository: TreatmentHistoryRepository = (
            TreatmentHistoryRepository()
        )
        self.user_repository: UserRepository = UserRepository()
        self.user_personal_info_repository = UserPersonalInfoRepository()
        self.image_for_analyzes_repository = ImageForAnalyzesRepository()
        self.treatment_history_image_for_analyzes_repository = (
            TreatmentHistoryImageForAnalyzesRepository()
        )

    def _get_response_data(self, treatment_history: TreatmentHistory, request) -> dict:
        image_for_analyzes = self.image_for_analyzes_repository.list(
            treatment_history=treatment_history
        )
        image_for_analyzes_serializer = ImageForAnlyzeSerializer(
            instance=image_for_analyzes, context={"request": request}, many=True
        )
        treatment_history_serializer = TreatmentHistorySerializer(
            instance=treatment_history
        )
        return {
            "treatment_history": treatment_history_serializer.data,
            "images_for_analyzes": image_for_analyzes_serializer.data,
        }

    def get(self, treatment_history_slug: str, request: HttpRequest) -> JsonResponse:
        if not self.treatment_history_repository.is_exist(
            treatment_history_slug=treatment_history_slug
        ):
            raise exceptions.ValidationError(
                detail={
                    "message": "Не валидные данные в запросе",
                    "description": f"Лечебная запись с slug {treatment_history_slug} не существует",
                },
            )

        treatment_history = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug,
        )
        return self._get_response_data(treatment_history, request)

    def list(
        self, patient_slug: str, doctor_specialization_slug: str = None, request=None
    ) -> list:
        if doctor_specialization_slug is not None:
            treatments_histories = self.treatment_history_repository.list(
                patient_slug=patient_slug,
                doctor_specialization_slug=doctor_specialization_slug,
            )
        else:
            treatments_histories = self.treatment_history_repository.list(
                patient_slug=patient_slug,
            )

        treatments_histories = [
            self._get_response_data(treatment_history, request)
            for treatment_history in treatments_histories
        ]
        return treatments_histories
