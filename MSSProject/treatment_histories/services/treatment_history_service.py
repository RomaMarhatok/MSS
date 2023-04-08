from django.http import JsonResponse
from django.db import transaction

from user.repositories import UserRepository
from user.serializers import UserPersonalInfoSerializer
from responses.errors import JsonResponseBadRequest
from doctor.repositories import DoctorRepository
from user.models import UserPersonalInfo
from ..models import TreatmentHistory
from ..repositories import (
    TreatmentHistoryRepository,
)
from ..serializers import TreatmentHistorySerializer, ImageForAnlyzeSerializer


class TreatmentHistoryService:
    def __init__(self) -> None:
        self.treatment_repository: TreatmentHistoryRepository = (
            TreatmentHistoryRepository()
        )
        self.user_repository: UserRepository = UserRepository()
        self.doctor_repository: DoctorRepository = DoctorRepository()

    def _response_formation(self, ts: TreatmentHistory, request):
        imgs = [
            tsifa.image_for_analyzes
            for tsifa in ts.treatment_history_image_for_analyzes.all()
        ]
        imgs_serialized = ImageForAnlyzeSerializer(
            instance=imgs, context={"request": request}, many=True
        ).data
        ts_serialized = TreatmentHistorySerializer(instance=ts).data
        return {
            "treatment_history": ts_serialized,
            "images_for_analyzes": imgs_serialized,
        }

    def get_patient_treatment_histories(
        self, patient_slug: str, doctor_specialization_slug: str, request=None
    ) -> JsonResponse:
        if not self.user_repository.is_exist(slug=patient_slug):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидные данные в запросе",
                    "description": "Пользователь с таким slug не существует",
                }
            )

        treatments_histories = self.treatment_repository.list(
            patient_slug=patient_slug,
            doctor_specialization_slug=doctor_specialization_slug,
        )

        tss = [self._response_formation(ts, request) for ts in treatments_histories]
        # TODO relocate in another repository or change on physical parameters
        try:
            user_personal_info = UserPersonalInfoSerializer(
                instance=treatments_histories[0].patient.userpersonalinfo,
                context={"request": request},
            ).data
        except UserPersonalInfo.DoesNotExist or IndexError:
            user_personal_info = {}
        # END TODO

        return JsonResponse(
            data={
                "patient_info": user_personal_info,
                "treatment_histories": tss,
            }
        )

    def get_patient_treatment_history(self, treatment_history_slug: str, request):
        if not self.treatment_repository.is_exist(
            treatment_history_slug=treatment_history_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидные данные в запросе",
                    "description": f"Лечебная запись с slug {treatment_history_slug} не существует",
                },
            )

        treatment_history = self.treatment_repository.get(
            treatment_history_slug=treatment_history_slug,
        )
        ts = self._response_formation(treatment_history, request)

        return JsonResponse(
            data={
                "treatment_history": ts,
            }
        )

    @transaction.atomic
    def create_treatment_history(self, data: dict):
        treatment_history = self.treatment_repository.create(data)
        serializer = TreatmentHistorySerializer(
            instance=treatment_history,
        )
        return JsonResponse(
            data={
                "treatment_history": serializer.data,
            }
        )
