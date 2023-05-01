from django.contrib import admin
from .models import PhysicalParameters

# Register your models here.


class AdminPhysicalParameters(admin.ModelAdmin):
    list_display = (
        "id",
        "slug",
        "user",
        "weight",
        "height",
        "pressure",
        "created_at",
    )
    search_fields = (
        "id",
        "slug",
    )


admin.site.register(PhysicalParameters, AdminPhysicalParameters)
