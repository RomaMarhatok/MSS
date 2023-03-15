from rest_framework.viewsets import GenericViewSet
from django.http import HttpRequest, JsonResponse
from ...services.treatment_history_service import TreatmentHistoryService
from userApp.permissions.is_doctor import IsDoctor
from userApp.permissions.is_user_authenticated import IsUserAuthenticated


class PatientTreatmentView(GenericViewSet):
    permission_classes = [IsUserAuthenticated, IsDoctor]

    def list(
        self, request: HttpRequest, patient_slug: str, doctor_specialization_slug: str
    ):
        service = TreatmentHistoryService()
        data = service.get_patient_treatment_histories(
            patient_slug, doctor_specialization_slug, request=request
        )
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )

    def retrieve(
        self,
        request: HttpRequest,
        patient_slug: str,
        treatment_slug: str,
    ):
        service = TreatmentHistoryService()
        data = service.get_treatment_history(patient_slug, treatment_slug)
        return JsonResponse(
            data=data["data"],
            status=data["status"],
        )
