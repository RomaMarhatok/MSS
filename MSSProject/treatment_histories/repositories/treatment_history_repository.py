from common.repository.base_repository import AbstractRepository
from ..models import TreatmentHistory
from userApp.repositories.doctor_repository import DoctorRepository
from django.db.models import QuerySet, Q

# user app imports
from user.models import User


class TreatmentHistoryRepository(AbstractRepository):
    def __init__(self):
        self.doctor_repository = DoctorRepository()
        self.__init_query = TreatmentHistory.objects.select_related(
            "doctor",
            "doctor__user",
            "doctor__user__role",
            "patient",
            "patient__user",
            "patient__user__role",
        )

    def list(self, **kwargs) -> QuerySet[TreatmentHistory]:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_specialization_slug = kwargs.get("doctor_specialization_slug", None)
        if patient_slug is None or doctor_specialization_slug is None:
            return None
        doctors_slugs = [
            doctor.user.slug
            for doctor, _ in self.doctor_repository.list(
                doctor_specialization_slug=doctor_specialization_slug
            )
        ]
        print(doctors_slugs)
        treatment_histories = self.__init_query.filter(
            Q(patient__user__slug=patient_slug)
            & Q(doctor__user__slug__in=doctors_slugs)
        ).order_by("-date")
        return treatment_histories

    def get(self, **kwargs) -> TreatmentHistory:
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        patient_slug = kwargs.get("patient_slug", None)
        if patient_slug is None or treatment_history_slug is None:
            return None
        treatment_history = self.__init_query.get(
            Q(patient__user__slug=patient_slug) & Q(slug=treatment_history_slug)
        )
        return treatment_history

    def is_exist(self, **kwargs) -> bool:
        treatment_history_slug = kwargs.get("treatment_history_slug", None)
        if treatment_history_slug is not None:
            return TreatmentHistory.objects.filter(slug=treatment_history_slug).exists()
        date = kwargs.get("date", None)
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        if date is not None and patient_slug is not None and doctor_slug is not None:
            return TreatmentHistory.objects.filter(
                Q(date=date)
                & Q(patient__user__slug=patient_slug)
                & Q(doctor__user__slug=doctor_slug)
            ).exists()
        return False

    def create(self, data: dict) -> None | TreatmentHistory:

        date = data.get("date", None)
        patient_slug = data.get("patient_slug", None)
        doctor_slug = data.get("doctor_slug", None)
        title = data.get("title", None)
        short_description = data.get("short_description", None)
        description = data.get("description", None)
        conclusion = data.get("conclusion", None)
        if not self.is_exist(
            date=date, patient_slug=patient_slug, doctor_slug=doctor_slug
        ):
            doctor, _ = self.doctor_repository.get(slug=doctor_slug)
            patient = User.objects.get(slug=patient_slug)
            return TreatmentHistory.objects.create(
                title=title,
                short_description=short_description,
                description=description,
                conclusion=conclusion,
                patient=patient,
                doctor=doctor,
            )

    def delete(self, **kwargs):
        return super().delete(**kwargs)
