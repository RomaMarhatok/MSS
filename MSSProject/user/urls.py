from django.urls import path
from user.views import (
    AuthenticationView,
    LogOutView,
    ProfileView,
    RegistrationView,
    UserPersonalInfoValidationView,
    UserValidationView,
    PatientView,
)

urlpatterns = [
    path(
        "profile/<str:user_slug>/",
        ProfileView.as_view({"get": "retrieve"}),
        name="user-profile",
    ),
    path(
        "authentication/",
        AuthenticationView.as_view(),
        name="user-authentication",
    ),
    path(
        "registration/",
        RegistrationView.as_view(),
        name="user-registration",
    ),
    path("logout/<str:user_slug>/", LogOutView.as_view(), name="user-logout"),
    path("validate/user/", UserValidationView.as_view(), name="validate-user"),
    path(
        "validate/info/", UserPersonalInfoValidationView.as_view(), name="validate-info"
    ),
    path(
        "patients/",
        PatientView.as_view({"get": "list"}),
        name="patients-list",
    ),
]
