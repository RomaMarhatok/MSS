from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "appointments"
    verbose_name = "Записи к врачам"

    def ready(self) -> None:
        from appointments.sheduler import start_appointment_email_sending

        start_appointment_email_sending()
        return super().ready()
