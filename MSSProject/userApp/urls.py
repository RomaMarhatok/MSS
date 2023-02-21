from django.urls import path, include
from userApp.views.patient.authentication_view import AuthenticationView
from userApp.views.patient.registration_view import RegistrationView
from userApp.views.patient.document_view import DocumentView
from userApp.views.patient.profile_view import ProfileView
from userApp.views.patient.doctor_view import DoctorView
from userApp.views.patient.doctor_specialization_view import DoctorSpecializationView
from userApp.views.patient.document_type_view import DocumentTypeView
from userApp.views.patient.appointments_view import AppointmentsView

# doctor view
from userApp.views.doctor.doctor_appointments_view import DoctorAppointments

urlpatterns = [
    path(
        "auth/registration/",
        RegistrationView.as_view(),
        name="token-user-registration",
    ),
    path(
        "auth/authentication/",
        AuthenticationView.as_view(),
        name="token-user-authentication",
    ),
    path(
        "doctors/",
        include(
            [
                path("", DoctorView.as_view({"get": "list"}), name="doctors-list"),
                path(
                    "specializations/",
                    DoctorSpecializationView.as_view(
                        {"get": "list"},
                    ),
                    name="doctor-types-list",
                ),
            ]
        ),
    ),
    path(
        "doctor/<str:doctor_slug>/",
        DoctorView.as_view({"get": "retrieve"}),
        name="doctor-retrieve",
    ),
    path(
        "user/<str:user_slug>/",
        include(
            [
                path(
                    "profile/",
                    ProfileView.as_view({"post": "retrieve"}),
                    name="user-profile",
                ),
                path(
                    "documents/",
                    DocumentView.as_view({"get": "list"}),
                    name="user-documents",
                ),
                path(
                    "document/<str:doc_slug>/",
                    DocumentView.as_view({"get": "retrieve"}),
                    name="user-document",
                ),
            ]
        ),
    ),
    path(
        "documents/types/",
        DocumentTypeView.as_view({"get": "list"}),
        name="list-document-types",
    ),
    path(
        "appointments/",
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
    path(
        "doctor/appointments/<str:doctor_slug>/",
        include(
            [
                path(
                    "",
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
]
