from ..models import Appointments
from ..serializers.appointments_serializer import AppointmentsSerializer
from .base import AbstractRepository
from django.db.models import Q, QuerySet


class AppointmentsRepository(AbstractRepository):
    def __init__(self):
        self.__init_query = Appointments.objects.select_related(
            "patient",
            "doctor",
            "patient__user",
            "doctor__user",
            "patient__user__role",
            "doctor__user__role",
            "doctor_specialization",
            "patient__user__userpersonalinfo",
            "doctor__user__userpersonalinfo",
        )

    def get(self, **kwargs) -> Appointments | None:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        date = kwargs.get("date", None)
        try:
            if (
                patient_slug is not None
                and doctor_slug is not None
                and date is not None
            ):
                return self.__init_query.get(
                    Q(patient__user__slug=patient_slug)
                    & Q(doctor__user__slug=doctor_slug)
                    & Q(date=date)
                )
            if patient_slug is not None and doctor_slug is not None:
                print(
                    "ASASA",
                    self.__init_query.get(
                        Q(patient__user__slug=patient_slug)
                        & Q(doctor__user__slug=doctor_slug)
                    ),
                )
                return self.__init_query.get(
                    Q(patient__user__slug=patient_slug)
                    & Q(doctor__user__slug=doctor_slug)
                )
        except Appointments.DoesNotExist:
            return None
        except Appointments.MultipleObjectsReturned:
            return None

    def list(self, **kwargs) -> QuerySet[Appointments] | None:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        if patient_slug is not None:
            return self.__init_query.filter(patient__user__slug=patient_slug)
        if doctor_slug is not None:
            return self.__init_query.filter(doctor__user__slug=doctor_slug)
        return None

    def create(self, data: dict) -> tuple[bool, Appointments] | tuple[bool, dict]:
        serializer = AppointmentsSerializer(data=data)
        if serializer.is_valid():
            appointment = serializer.save()
            return (
                True,
                appointment,
            )
        return (
            False,
            serializer.errors,
        )

    def delete(self, **kwargs) -> int | None:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        date = kwargs.get("date", None)
        if patient_slug is None or doctor_slug is None or date is None:
            return None
        instance = Appointments.objects.filter(
            doctor__user__slug=doctor_slug, patient__user__slug=patient_slug, date=date
        )
        if instance.exists():
            count_of_deleted_instantes, _ = instance.first().delete()
            return count_of_deleted_instantes
        return None

    def is_exist(self, **kwargs) -> bool:
        patient_slug = kwargs.get("patient_slug", None)
        doctor_slug = kwargs.get("doctor_slug", None)
        date = kwargs.get("date", None)
        print(patient_slug, doctor_slug, date)
        if patient_slug is None or doctor_slug is None or date is None:
            return None
        return Appointments.objects.filter(
            Q(patient__user__slug=patient_slug)
            & Q(doctor__user__slug=doctor_slug)
            & Q(date=date)
        ).exists()
