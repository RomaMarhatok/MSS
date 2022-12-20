from django.urls import path, include
from userApp.views.authentication_view import AuthenticationView
from userApp.views.registration_view import RegistrationView
from userApp.views.document_view import DocumentView
from userApp.views.profile_view import ProfileView

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
]
