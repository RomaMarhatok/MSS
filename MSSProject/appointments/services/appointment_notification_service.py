from datetime import datetime, timedelta
from django.db.models import QuerySet
from user.services import EmailService
from ..repositories import AppointmentsRepository
from ..models import Appointments
from common.utils.date_utils import parse_date_to_str


class AppointmentNotificationService(EmailService):
    def __init__(self) -> None:
        super().__init__()
        self.appointment_repository = AppointmentsRepository()

    def _get_mail_subject(self):
        return "Скорые записи к врачам!"

    def _get_soon_appointments(self) -> QuerySet[Appointments]:
        notification_date = datetime.now() + timedelta(days=2)
        appointments = self.appointment_repository.get_appointment_by_date(
            notification_date
        )
        return appointments

    def _get_message(self, appointments: QuerySet[Appointments]) -> str:
        message = "У вас скорый прием у следующих врачей:\n"
        for i, appointment in enumerate(appointments):
            if hasattr(appointment.doctor.user, "userpersonalinfo"):
                doctor_full_name = appointment.doctor.user.userpersonalinfo.full_name
                message += (
                    str(i + 1)
                    + ". "
                    + "У "
                    + doctor_full_name
                    + " "
                    + f"специализация:{appointment.doctor_specialization.name}"
                    + " в "
                    + parse_date_to_str(appointment.date)
                    + "\n"
                )
        return message

    def send_notifications(self):
        appointments = self._get_soon_appointments()
        mail_subject = self._get_mail_subject()
        black_list_emails = []
        for appointment in appointments:
            patient = appointment.patient
            if hasattr(patient, "userpersonalinfo"):
                email = patient.userpersonalinfo.email
                print(f"SEND EMAIL TO: {email}")
                if email not in black_list_emails:
                    connection = self.get_email_connection(email, fail_silently=True)
                    print(f"CONNECTION: {connection}")
                    if connection is None:
                        continue
                    from_email = self._get_from_email(connection)
                    patient_appointments = appointments.filter(patient=patient)
                    email_message = self._get_message(patient_appointments)
                    black_list_emails.append(email)
                    print(f"EMAL MESSAGE: {email_message}")
                    self._send(
                        mail_subject,
                        email_message,
                        from_email,
                        [email],
                        connection,
                    )

    def foo(self):
        print("FOO")
        data = {"link": "Test", "email": "r.marhatok@yandex.by"}
        EmailService().send(data)
