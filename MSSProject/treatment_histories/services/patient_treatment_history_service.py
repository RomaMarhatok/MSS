from django.http import JsonResponse
from .base.base_treatment_history_service import BaseTreatmentHistoryService


class PatientTreatmentHistoryService(BaseTreatmentHistoryService):
    def get_user_treatments_histories_list(
        self, patient_slug: str, request
    ) -> JsonResponse:
        # проверка существования пользователя
        if self.is_user_exist(patient_slug):
            # запрос лечеьбных историй пользователя
            treatments_histories = self.list(patient_slug, request=request)
        # формирование ответа
        return JsonResponse(
            data={
                "treatment_histories": treatments_histories,
            }
        )

    def get_user_treatments_history(self, treatment_history_slug: str, request):
        return JsonResponse(data=self.get(treatment_history_slug, request))
