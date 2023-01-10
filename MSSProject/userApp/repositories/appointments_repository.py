from django.db.models import Q
from ..models import Appointments, Doctor, Patient
from ..serializers.appointments_serializer import AppointmentsSerializer


class AppointmentsRepository:
    def get_list_of_appoitments(self, user_slug: str) -> list:
        isntances = Appointments.objects.filter(
            patient__user__slug=user_slug
        ).select_related(
            "patient",
            "doctor",
            "patient__user",
            "doctor__user",
        )

        return AppointmentsSerializer(instance=isntances, many=True).data

    def get_appoitment(self, user_slug: str, doctor_slug: str) -> dict:
        instance = (
            Appointments.objects.filter(
                Q(patient__user__slug=user_slug) & Q(doctor__user__slug=doctor_slug)
            )
            .select_related(
                "patient",
                "doctor",
                "patient__user",
                "doctor__user",
            )
            .first()
        )
        return AppointmentsSerializer(instance=instance).data

    def create_appointment(self, data: dict) -> tuple[dict | None, bool]:
        serializer = AppointmentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return (
                None,
                True,
            )
        return (
            serializer.errors,
            False,
        )

    def delete_appointment(self, doctor: Doctor = None, patient: Patient = None) -> int:
        instance = Appointments.objects.filter(doctor=doctor, patient=patient)
        if instance.exists():
            count_of_deleted_instantes, _ = instance.first().delete()
            return count_of_deleted_instantes
        return None
