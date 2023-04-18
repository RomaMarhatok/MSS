from django.http import JsonResponse, HttpRequest
from django.db import transaction

from user.repositories import UserRepository, UserPersonalInfoRepository
from user.serializers import UserPersonalInfoSerializer
from user.services.mixins.is_user_exist_mixin import IsUserExistMixin
from responses.errors import JsonResponseBadRequest
from user.models import UserPersonalInfo
from ..models import TreatmentHistory, ImageForAnalyzes
from ..repositories import (
    TreatmentHistoryRepository,
    ImageForAnalyzesRepository,
    TreatmentHistoryImageForAnalyzesRepository,
)
from ..serializers import TreatmentHistorySerializer, ImageForAnlyzeSerializer


class TreatmentHistoryService(IsUserExistMixin):
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

    def _response_formation(self, ts: TreatmentHistory, request):
        imgs = [
            tsifa.image_for_analyzes
            for tsifa in ts.treatment_history_image_for_analyzes.all()
        ]
        imgs_serialized = ImageForAnlyzeSerializer(
            instance=imgs, context={"request": request}, many=True
        ).data
        ts_serialized = TreatmentHistorySerializer(instance=ts).data
        ts_serialized.update({"count_of_images": len(imgs)})
        return {
            "treatment_history": ts_serialized,
            "images_for_analyzes": imgs_serialized,
        }

    def _get(self, treatment_history_slug: str, request: HttpRequest) -> JsonResponse:
        if not self.treatment_history_repository.is_exist(
            treatment_history_slug=treatment_history_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидные данные в запросе",
                    "description": f"Лечебная запись с slug {treatment_history_slug} не существует",
                },
            )

        treatment_history = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug,
        )
        return self._response_formation(treatment_history, request)

    def _list(
        self, patient_slug: str, doctor_specialization_slug: str = None, request=None
    ) -> list:
        if doctor_specialization_slug is not None:
            treatments_histories_qs = self.treatment_history_repository.list(
                patient_slug=patient_slug,
                doctor_specialization_slug=doctor_specialization_slug,
            )

            treatments_histories = [
                self._response_formation(ts, request) for ts in treatments_histories_qs
            ]
            return treatments_histories
        treatments_histories_qs = self.treatment_history_repository.list(
            patient_slug=patient_slug,
        )
        treatments_histories = [
            self._response_formation(ts, request) for ts in treatments_histories_qs
        ]
        return treatments_histories

    def get_patient_treatment_histories_list(
        self, patient_slug: str, doctor_specialization_slug: str, request=None
    ) -> JsonResponse:
        response = self.user_exist(patient_slug)
        if response.status_code == 400:
            return response
        treatments_histories = self._list(
            patient_slug,
            doctor_specialization_slug=doctor_specialization_slug,
            request=request,
        )
        user = self.user_repository.get(slug=patient_slug)
        try:
            user_personal_info = self.user_personal_info_repository.get(slug=user.slug)
            patient_info = UserPersonalInfoSerializer(instance=user_personal_info).data
        except UserPersonalInfo.DoesNotExist:
            patient_info = {}
        return JsonResponse(
            data={
                "patient_info": patient_info,
                "treatment_histories": treatments_histories,
            }
        )

    def get_user_treatments_histories_list(
        self, patient_slug: str, request
    ) -> JsonResponse:
        response = self.user_exist(patient_slug)
        if response.status_code == 400:
            return response
        treatments_histories = self._list(patient_slug)
        return JsonResponse(
            data={
                "treatment_histories": treatments_histories,
            }
        )

    def get_patient_treatment_history(self, treatment_history_slug: str, request):
        return self._get(treatment_history_slug, request)

    def get_user_treatments_history(self, treatment_history_slug: str, request):
        return self._get(treatment_history_slug, request)

    @transaction.atomic
    def create_treatment_history(self, data: dict):
        treatment_history_qs = self.treatment_history_repository.create(data)
        serialized_ts = TreatmentHistorySerializer(instance=treatment_history_qs).data
        serialized_ts.update({"count_of_images": 0})
        return JsonResponse(data={"treatment_history": serialized_ts})

    @transaction.atomic
    def create_image_for_analyzes(self, data: dict):
        treatment_history_slug = data.get("treatment_history_slug", None)
        treatment_history = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug
        )
        img_qs = self.image_for_analyzes_repository.create(data)
        serializerd_img = ImageForAnlyzeSerializer(instance=img_qs).data
        self.create_union_table(treatment_history, img_qs)
        return JsonResponse(data={"image_for_analyze": serializerd_img})

    @transaction.atomic
    def create_union_table(
        self, treatment_history: TreatmentHistory, img: ImageForAnalyzes
    ) -> None:
        self.treatment_history_image_for_analyzes_repository.create(
            {"treatment_history": treatment_history, "image_for_analyzes": img}
        )

    @transaction.atomic
    def update_treatment_history(self, data: dict):
        treatment_history_slug = data.get("treatment_history_slug", None)
        if not self.treatment_history_repository.is_exist(
            treatment_history_slug=treatment_history_slug
        ):
            return JsonResponseBadRequest(
                data={
                    "message": "Не валидные данные в запросе",
                    "description": f"Лечебная запись с slug {treatment_history_slug} не существует",
                }
            )
        treatment_history_qs = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug
        )
        ts = self.treatment_history_repository.update(data, treatment_history_qs)
        serialized_ts = TreatmentHistorySerializer(instance=ts).data
        return JsonResponse(data={"treatment_history": serialized_ts})

    @transaction.atomic
    def delete_img_for_analyzes(self, data: dict):
        request = data.get("request", None)
        treatment_history_slug = data.get("treatment_history_slug", None)
        ts = self.treatment_history_repository.get(
            treatment_history_slug=treatment_history_slug
        )
        image_for_analyzes_slug = data.get("image_for_analyzes_slug", None)
        img_for_analyzes = self.image_for_analyzes_repository.get(
            slug=image_for_analyzes_slug
        )
        self.treatment_history_image_for_analyzes_repository.delete(
            ts=ts, img=img_for_analyzes
        )
        img_for_analyzes.delete()
        return self._get(
            ts.slug,
            request,
        )
