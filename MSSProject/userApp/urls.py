from rest_framework.routers import DefaultRouter
from django.urls import path
from userApp.views import TokenRegistrationView, TokenAuthenticationView

urlpatterns = [
    path(
        "auth/registration/",
        TokenRegistrationView.as_view(),
        name="token-user-registration",
    ),
    path(
        "auth/authentication/",
        TokenAuthenticationView.as_view(),
        name="token-user-authentication",
    ),
]
