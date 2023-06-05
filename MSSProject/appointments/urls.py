from django.urls import path, include
from appointments.views import DoctorAppointmentsView, PatientAppointmentsView


urlpatterns = [
    path(
        "doctor/",
        include(
            [
                path(
                    "create/",
                    DoctorAppointmentsView.as_view({"post": "create"}),
                    name="doctor-appointments-create",
                ),
                path(
                    "destroy/",
                    DoctorAppointmentsView.as_view({"post": "destroy"}),
                    name="doctor-appointments-destroy",
                ),
                path(
                    "appointments/<str:doctor_slug>/",
                    DoctorAppointmentsView.as_view({"get": "list"}),
                    name="doctor-appoitments-list",
                ),
                path(
                    "<str:patient_slug>/",
                    DoctorAppointmentsView.as_view({"get": "retrieve"}),
                    name="doctor-appoitments-retrieve",
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
                    PatientAppointmentsView.as_view({"post": "destroy"}),
                    name="patient-appointments-destroy",
                ),
                path(
                    "create/",
                    PatientAppointmentsView.as_view({"post": "create"}),
                    name="patient-appointments-create",
                ),
                path(
                    "<str:patient_slug>/",
                    PatientAppointmentsView.as_view({"get": "list"}),
                    name="patient-appoitments-list",
                ),
                path(
                    "<str:patient_slug>/<str:doctor_slug>/",
                    PatientAppointmentsView.as_view({"get": "retrieve"}),
                    name="patient-appoitments-retrieve",
                ),
            ]
        ),
    ),
]
