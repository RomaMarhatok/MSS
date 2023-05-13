from apscheduler.schedulers.background import BackgroundScheduler
from .services import AppointmentNotificationService

appointment_notification_service = AppointmentNotificationService()


def start_appointment_email_sending():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        appointment_notification_service.send_notifications,
        "interval",
        hours=23,
    )
    scheduler.start()
