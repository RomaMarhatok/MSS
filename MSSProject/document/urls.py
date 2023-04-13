from django.urls import path
from document.views import DocumentTypeView, DocumentView, NewestDocumentView

urlpatterns = [
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
        DocumentView.as_view({"get": "list"}),
        name="list-user-documents",
    ),
    path(
        "document/<str:user_slug>/<str:doc_slug>/",
        DocumentView.as_view({"get": "retrieve"}),
        name="retrieve-user-document",
    ),
    path(
        "create/",
        DocumentView.as_view({"post": "create"}),
        name="create-user-document",
    ),
]
