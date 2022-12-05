from rest_framework.routers import DefaultRouter
from django.urls import include, path
from views import TokenRegistrationView

urlpatterns = [
    path(
        "registration/", TokenRegistrationView.as_view(), name="token-user-registration"
    )
]
