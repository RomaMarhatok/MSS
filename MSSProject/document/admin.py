from django.contrib import admin
from .models import Document, DocumentType

# Start Document Models


class AdminDocumentType(admin.ModelAdmin):
    search_fields = (
        "slug",
        "name",
    )
    list_display = (
        "id",
        "slug",
        "name",
    )


admin.site.register(DocumentType, AdminDocumentType)


class AdminDocument(admin.ModelAdmin):
    search_fields = (
        "slug",
        "name",
        "document_type",
    )
    list_display = (
        "id",
        "slug",
        "name",
        "document_type",
    )


admin.site.register(Document, AdminDocument)

# End Docuemnt Models
