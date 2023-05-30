from django.contrib import admin
from .models import (
    Doctor,
    DoctorSummary,
    DoctorDoctorSpecialization,
    DoctorSpecialization,
)

# Start Doctor Models


class AdminDoctor(admin.ModelAdmin):
    search_fields = ("user",)
    readonly_fields = ("user",)
    list_display = ("user",)


admin.site.register(Doctor, AdminDoctor)


# class AdminDoctorSummary(admin.ModelAdmin):
#     search_fields = ("doctor",)
#     list_display = ("doctor",)
#     list_display_links = ("doctor",)


# admin.site.register(DoctorSummary, AdminDoctorSummary)


class AdminDoctorSpecialization(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = (
        "id",
        "name",
        "slug",
    )
    search_fields = (
        "id",
        "name",
        "slug",
    )


admin.site.register(DoctorSpecialization, AdminDoctorSpecialization)


class AdminDoctorDoctorSpecialization(admin.ModelAdmin):
    list_display = (
        "doctor",
        "doctor_specialization",
    )
    list_display_links = (
        "doctor",
        "doctor_specialization",
    )
    search_fields = (
        "doctor",
        "doctor_specialization",
    )


admin.site.register(DoctorDoctorSpecialization, AdminDoctorDoctorSpecialization)

# End Doctor Models
