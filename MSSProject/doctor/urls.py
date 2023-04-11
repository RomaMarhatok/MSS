from django.urls import path, include
from doctor.views import DoctorView, DoctorSpecializationView

urlpatterns = [
    path("list/", DoctorView.as_view({"get": "list"}), name="doctors-list"),
    path(
        "specializations/",
        DoctorSpecializationView.as_view(
            {"get": "list"},
        ),
        name="doctor-types-list",
    ),
    path("<str:doctor_slug>/", DoctorView.as_view({"get": "retrieve"})),
]
