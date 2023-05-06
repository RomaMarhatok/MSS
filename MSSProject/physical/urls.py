from django.urls import path
from physical.views import PhysicalParametersView

urlpatterns = [
    path(
        "update/",
        PhysicalParametersView.as_view({"post": "update"}),
        name="physical-update",
    ),
    path(
        "create/",
        PhysicalParametersView.as_view({"post": "create"}),
        name="physical-create",
    ),
    path(
        "delete/",
        PhysicalParametersView.as_view({"post": "delete"}),
        name="physical-delete",
    ),
    path(
        "list/<str:patient_slug>/",
        PhysicalParametersView.as_view({"get": "list"}),
        name="physical-list",
    ),
    path(
        "get/<str:slug>/",
        PhysicalParametersView.as_view({"get": "retrieve"}),
        name="physical-retrieve",
    ),
]
