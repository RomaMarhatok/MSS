from rest_framework.viewsets import GenericViewSet
from django.http import HttpRequest, JsonResponse
from userApp.services.model_services.treatment_history_service import (
    TreatmentHistoryService,
)


class PatientTreatmentView(GenericViewSet):
    def list(self, request: HttpRequest, patient_slug: str):
        print(1)
        service = TreatmentHistoryService()
        data = service.get_treatment_histories(patient_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(self, request: HttpRequest, patient_slug: str, treatment_slug: str):
        service = TreatmentHistoryService()
        data = service.get_treatment_history(patient_slug, treatment_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )
