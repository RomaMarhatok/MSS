from django.urls import path, include
from userApp.views.authentication_view import AuthenticationView
from userApp.views.registration_view import RegistrationView
from userApp.views.document_view import DocumentView
from userApp.views.profile_view import ProfileView
from userApp.views.doctor_view import DoctorView
from userApp.views.doctor_specialization_view import DoctorSpecializationView
from userApp.views.document_type_view import DocumentTypeView

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
]
