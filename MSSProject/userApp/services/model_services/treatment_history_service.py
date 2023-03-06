from rest_framework import status
from userApp.repositories.treatment_history_repository import TreatmentHistoryRepository
from userApp.repositories.user_repository import UserRepository


class TreatmentHistoryService:
    treatment_repository: TreatmentHistoryRepository = TreatmentHistoryRepository()
    user_repository: UserRepository = UserRepository()

    def get_patient_treatment_histories(
        self, patient_slug: str, doctor_specialization_slug: str
    ):
        if self.user_repository.is_user_exist_by_slug(patient_slug):
            treatments_histories = self.treatment_repository.get_treatments_histories(
                patient_slug, doctor_specialization_slug
            )
            return {
                "data": {"treatment_histories": treatments_histories},
                "status": status.HTTP_200_OK,
            }
        return {"data": ["patient don't exist"], "status": status.HTTP_404_NOT_FOUND}

    def get_treatment_histories_by_doctor_specialization(
        self, patient_slug: str, doctor_specialization_slug: str
    ):
        if self.user_repository.is_user_exist_by_slug(patient_slug):
            treatments_histories = self.treatment_repository.get_treatments_histories(
                patient_slug, doctor_specialization_slug
            )
            return {
                "data": {"treatment_histories": treatments_histories},
                "status": status.HTTP_200_OK,
            }
        return {"data": ["patient don't exist"], "status": status.HTTP_404_NOT_FOUND}

    def get_treatment_history(self, patient_slug: str, treatment_slug):
        if self.user_repository.is_user_exist_by_slug(patient_slug):
            if self.treatment_repository.treatment_record_exist(treatment_slug):
                treatment = self.treatment_repository.get_treatment_history(
                    patient_slug, treatment_slug
                )
                return {"data": treatment, "status": status.HTTP_200_OK}
            return {
                "data": {"errors": ["treatment history don't exist"]},
                "status": status.HTTP_404_NOT_FOUND,
            }
        return {
            "data": {"errors": ["patient don't exist"]},
            "status": status.HTTP_404_NOT_FOUND,
        }
