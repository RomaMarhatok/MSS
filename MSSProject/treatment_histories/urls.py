from django.urls import path
from treatment_histories.views import (
    PatientTreatmentsView,
    UserTreatmentHistoriesView,
    CreateImageForAnalyzesView,
    CreateTreatmentHistoryView,
    UpdateTreatmentHistoryView,
)

urlpatterns = [
    path(
        "treatment/patient/<str:patient_slug>/",
        UserTreatmentHistoriesView.as_view({"get": "list"}),
        name="patient-treatment-history-list",
    ),
    path(
        "treatments/patient/<str:treatment_slug>/",
        UserTreatmentHistoriesView.as_view({"get": "retrieve"}),
        name="patient-treatment-history-retrieve",
    ),
    path(
        "treatments/<str:patient_slug>/<str:doctor_specialization_slug>/",
        PatientTreatmentsView.as_view({"get": "list"}),
        name="treatment-history-list",
    ),
    path(
        "treatment/<str:treatment_slug>/",
        PatientTreatmentsView.as_view({"get": "retrieve"}),
        name="treatment-history-retrieve",
    ),
    path(
        "create/",
        CreateTreatmentHistoryView.as_view(),
        name="treatment-history-create",
    ),
    path(
        "create/image/",
        CreateImageForAnalyzesView.as_view(),
        name="create-image-for-analyzes",
    ),
    path(
        "update/",
        UpdateTreatmentHistoryView.as_view(),
        name="update-treatment-history",
    ),
]
