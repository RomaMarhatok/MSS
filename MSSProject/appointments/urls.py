from django.urls import path, include
from appointments.views import DoctorAppointments, AppointmentsView


urlpatterns = [
    path(
        "doctor/",
        include(
            [
                path(
                    "appointments/<str:doctor_slug>/",
                    DoctorAppointments.as_view({"get": "list"}),
                    name="appoitments-list",
                ),
                path(
                    "<str:patient_slug>/",
                    DoctorAppointments.as_view({"get": "retrieve"}),
                    name="appoitments-retrieve",
                ),
            ]
        ),
    ),
    path(
        "patient/",
        include(
            [
                path(
                    "destroy/",
                    AppointmentsView.as_view({"post": "destroy"}),
                    name="appointments-destroy",
                ),
                path(
                    "create/",
                    AppointmentsView.as_view({"post": "create"}),
                    name="appointments-create",
                ),
                path(
                    "<str:patient_slug>/",
                    AppointmentsView.as_view({"get": "list"}),
                    name="appoitments-list",
                ),
                path(
                    "<str:patient_slug>/<str:doctor_slug>/",
                    AppointmentsView.as_view({"get": "retrieve"}),
                    name="appoitments-retrieve",
                ),
            ]
        ),
    ),
]
