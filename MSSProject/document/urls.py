from django.urls import path
from document.views import (
    DocumentTypeView,
    PatientDocumentView,
    NewestDocumentView,
    DoctorDocumentView,
)

urlpatterns = [
    path(
        "doctor/documents/<str:creator_slug>/",
        DoctorDocumentView.as_view({"get": "list"}),
        name="doctor-list-documents",
    ),
    path(
        "doctor/document/<str:creator_slug>/<str:doc_slug>/",
        DoctorDocumentView.as_view({"get": "retrieve"}),
        name="doctor-retrieve-document",
    ),
    path(
        "delete/",
        DoctorDocumentView.as_view({"post": "delete"}),
        name="doctor-delete-document",
    ),
    path(
        "create/",
        DoctorDocumentView.as_view({"post": "create"}),
        name="create-user-document",
    ),
    path(
        "update/",
        DoctorDocumentView.as_view({"post": "update"}),
        name="update-user-document",
    ),
    path(
        "new/<str:patient_slug>/",
        NewestDocumentView.as_view(),
        name="newest-patient-document",
    ),
    path(
        "documents/types/",
        DocumentTypeView.as_view({"get": "list"}),
        name="list-document-types",
    ),
    path(
        "documents/<str:user_slug>/",
        PatientDocumentView.as_view({"get": "list"}),
        name="list-user-documents",
    ),
    path(
        "document/<str:user_slug>/<str:doc_slug>/",
        PatientDocumentView.as_view({"get": "retrieve"}),
        name="retrieve-user-document",
    ),
]
