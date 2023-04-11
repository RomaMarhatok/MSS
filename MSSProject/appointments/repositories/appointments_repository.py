from ..models import Appointments
from ..serializers.appointments_serializer import AppointmentsSerializer
from common.repository.base_repository import AbstractRepository
from django.db.models import Q, QuerySet


class AppointmentsRepository(AbstractRepository):
    def __init__(self):
        self.__init_query = Appointments.objects.select_related(
            "patient",
            "doctor",
            "patient",
            "doctor__user",
            "patient__role",
            "doctor__user__role",
            "doctor_specialization",
            "patient__userpersonalinfo",
            "doctor__user__userpersonalinfo",
        )

    def get(self, **kwargs) -> Appointments | None:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        date = kwargs.get("date", None)
        if patient_slug is not None and doctor_slug is not None and date is not None:
            return self.__init_query.get(
                Q(patient__slug=patient_slug)
                & Q(doctor__user__slug=doctor_slug)
                & Q(date=date)
            )
        if patient_slug is not None and doctor_slug is not None:
            return self.__init_query.get(
                Q(patient__slug=patient_slug) & Q(doctor__user__slug=doctor_slug)
            )

    def list(self, **kwargs) -> QuerySet[Appointments] | None:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        if patient_slug is not None:
            return self.__init_query.filter(patient__slug=patient_slug)
        if doctor_slug is not None:
            return self.__init_query.filter(doctor__user__slug=doctor_slug)

    def create(self, data: dict) -> Appointments:
        serializer = AppointmentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()

    def delete(self, **kwargs) -> int:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        date = kwargs.get("date", None)
        if patient_slug is None or doctor_slug is None or date is None:
            return None
        count_of_deleted_instantes, _ = Appointments.objects.filter(
            doctor__user__slug=doctor_slug, patient__slug=patient_slug, date=date
        ).delete()
        return count_of_deleted_instantes

    def is_exist(self, **kwargs) -> bool:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        date = kwargs.get("date", None)
        if patient_slug is None or doctor_slug is None or date is None:
            return None
        return Appointments.objects.filter(
            Q(patient__slug=patient_slug)
            & Q(doctor__user__slug=doctor_slug)
            & Q(date=date)
        ).exists()
