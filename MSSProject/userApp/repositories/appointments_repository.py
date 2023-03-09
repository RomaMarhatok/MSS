from django.db.models import Q
from ..models import Appointments, Doctor, Patient
from ..serializers.appointments_serializer import AppointmentsSerializer


class AppointmentsRepository:
    def get_list_of_appoitments_for_patient(self, user_slug: str) -> list:
        instances = (
            Appointments.objects.filter(patient__user__slug=user_slug)
            .select_related(
                "patient",
                "doctor",
                "patient__user",
                "doctor__user",
            )
            .order_by("-date")
        )

        appointments = AppointmentsSerializer(instance=instances, many=True).data
        return appointments

    def get_list_of_appointemnts_for_doctor(self, doctor_slug: str) -> list:
        instances = (
            Appointments.objects.filter(doctor__user__slug=doctor_slug)
            .select_related(
                "patient",
                "doctor",
                "patient__user",
                "doctor__user",
            )
            .order_by("date")
        )
        appointments = AppointmentsSerializer(
            instance=instances, many=True, context={"is_doctor": True}
        ).data
        return appointments

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
        appointment = AppointmentsSerializer(instance=instance).data
        return appointment

    def is_exist(self, user_slug: str, doctor_slug: str, appointment_date: str) -> bool:
        is_exist = Appointments.objects.filter(
            Q(patient__user__slug=user_slug)
            & Q(doctor__user__slug=doctor_slug)
            & Q(date=appointment_date)
        ).exists()
        if not is_exist:
            is_exist = Appointments.objects.filter(
                Q(patient__user__slug=user_slug) & Q(doctor__user__slug=doctor_slug)
            ).exists()
        return is_exist

    def create_appointment(self, data: dict) -> tuple[dict, bool]:
        serializer = AppointmentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            appointment = serializer.save()
            serialized_appointment = AppointmentsSerializer(instance=appointment).data
            return (
                serialized_appointment,
                True,
            )
        return (
            serializer.errors,
            False,
        )

    def delete_appointment(
        self, doctor: Doctor = None, patient: Patient = None
    ) -> int | None:
        instance = Appointments.objects.filter(doctor=doctor, patient=patient)
        if instance.exists():
            count_of_deleted_instantes, _ = instance.first().delete()
            return count_of_deleted_instantes
        return None
