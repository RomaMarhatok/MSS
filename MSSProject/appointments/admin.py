from django.contrib import admin
from .models import Appointments

# Start Appointments Models


class AdminAppointments(admin.ModelAdmin):
    list_display = (
        "doctor",
        "doctor_specialization",
        "patient",
        "date",
    )
    list_display_links = (
        "doctor",
        "doctor_specialization",
        "patient",
        "date",
    )
    search_fields = (
        "doctor",
        "doctor_specialization",
        "patient",
        "date",
    )


admin.site.register(Appointments, AdminAppointments)
# End Appointments Models
