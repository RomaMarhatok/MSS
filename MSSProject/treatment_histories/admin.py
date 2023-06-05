from django.contrib import admin
from .models import (
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
    ImageForAnalyzes,
    TreatmentHistoryDocument,
)

# Start Treatment History Models


class AdminTreatmentHistory(admin.ModelAdmin):
    search_fields = (
        "slug",
        "title",
        "date",
        "doctor",
        "patient",
    )
    list_display = (
        "slug",
        "title",
        "date",
        "doctor",
        "patient",
    )
    list_display_links = (
        "slug",
        "title",
        "date",
        "doctor",
        "patient",
    )


admin.site.register(TreatmentHistory, AdminTreatmentHistory)


class AdminImageForAnalyzes(admin.ModelAdmin):
    list_display = ("image",)


admin.site.register(ImageForAnalyzes, AdminImageForAnalyzes)


class AdminTreatmentHistoryImageForAnalyzes(admin.ModelAdmin):
    list_display = (
        "treatment_history",
        "image_for_analyzes",
    )
    search_fields = (
        "treatment_history",
        "image_for_analyzes",
    )
    list_display_links = (
        "treatment_history",
        "image_for_analyzes",
    )


admin.site.register(
    TreatmentHistoryImageForAnalyzes, AdminTreatmentHistoryImageForAnalyzes
)


class AdminTreatmentHistoryDocument(admin.ModelAdmin):
    list_display = (
        "treatment_history",
        "document",
    )
    search_fields = (
        "treatment_history",
        "document",
    )
    list_display_links = (
        "treatment_history",
        "document",
    )


admin.site.register(TreatmentHistoryDocument, AdminTreatmentHistoryDocument)

# End Treatment History Models
