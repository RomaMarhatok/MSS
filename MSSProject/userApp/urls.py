from django.urls import path
from userApp.views.authentication_view import AuthenticationView
from userApp.views.registration_view import RegistrationView

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
]
