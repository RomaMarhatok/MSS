from django.urls import path
from document.views import DocumentTypeView, DocumentView

urlpatterns = [
    path(
        "documents/<str:user_slug>/",
        DocumentView.as_view({"get": "list"}),
        name="user-documents",
    ),
    path(
        "document/<str:user_slug>/<str:doc_slug>/",
        DocumentView.as_view({"get": "retrieve"}),
        name="user-document",
    ),
    path(
        "documents/types/",
        DocumentTypeView.as_view({"get": "list"}),
        name="list-document-types",
    ),
]
