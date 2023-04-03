from django.urls import path, include
from treatment_histories.views import PatientTreatmentView

urlpatterns = [
    path(
        "treatments/<str:patient_slug>/<str:doctor_specialization_slug>/",
        PatientTreatmentView.as_view({"get": "list"}),
        name="treatment-history-list",
    ),
    path(
        "treatment/<str:patient_slug>/<str:treatment_slug>/",
        PatientTreatmentView.as_view({"get": "retrieve"}),
        name="treatment-history-retrieve",
    ),
    path(
        "create/",
        PatientTreatmentView.as_view({"post": "create"}),
        name="treatment-history-create",
    ),
]
