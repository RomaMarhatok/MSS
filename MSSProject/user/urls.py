from django.urls import path, include
from user.views import ProfileView, AuthenticationView, RegistrationView, LogOutView

urlpatterns = [
    path(
        "profile/<str:user_slug>/",
        ProfileView.as_view({"get": "retrieve"}),
        name="user-profile",
    ),
    path(
        "authentication/",
        AuthenticationView.as_view(),
        name="token-user-authentication",
    ),
    path(
        "registration/",
        RegistrationView.as_view(),
        name="user-registration",
    ),
    path("logout/", LogOutView.as_view(), name="user-logout"),
]
