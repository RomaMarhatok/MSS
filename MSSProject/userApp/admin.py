from django.contrib import admin
from .models import (
    Role,
    User,
    UserPersonalInfo,
    UserLocation,
    Patient,
    Doctor,
    DocumentType,
    Document,
    DoctorSummary,
    DocumentCreator,
    DoctorSpecialization,
    TreatmentHistory,
    TreatmentHistoryImageForAnalyzes,
    ImageForAnalyzes,
    Appointments,
    DoctorDoctorSpecialization,
)


admin.site.site_header = "MSS Admin Panel"
admin.site.site_title = "MSS Admin Panel"
# Start Role Model


class AdminRole(admin.ModelAdmin):
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


admin.site.register(Role, AdminRole)

# End Role Model

# Start User Models


class AdminUser(admin.ModelAdmin):
    list_display = ("id", "login", "password", "slug", "role")
    list_display_links = (
        "id",
        "login",
        "slug",
    )
    search_fields = ("id", "login", "slug", "role")
    exclude = (
        "first_name",
        "username",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "user_permissions",
        "groups",
        "last_login",
    )


admin.site.register(User, AdminUser)


class AdminUserPersonalInfo(admin.ModelAdmin):
    search_fields = ("user",)
    readonly_fields = ("user",)
    list_display = (
        "id",
        "user",
        "first_name",
        "second_name",
        "patronymic",
        "gender",
        "age",
    )


admin.site.register(UserPersonalInfo, AdminUserPersonalInfo)


class AdminUserLocation(admin.ModelAdmin):
    search_fields = ("user",)
    readonly_fields = ("user",)
    list_display = (
        "id",
        "user",
        "city",
        "address",
        "country",
    )


admin.site.register(UserLocation, AdminUserLocation)
# End User Models

# Start Patient Models


class AdminPatient(admin.ModelAdmin):
    search_fields = ("user",)
    readonly_fields = ("user",)
    list_display = ("user",)


admin.site.register(Patient, AdminPatient)

# End Patient Models

# Start Doctor Models


class AdminDoctor(admin.ModelAdmin):
    search_fields = ("user",)
    readonly_fields = ("user",)
    list_display = ("user",)


admin.site.register(Doctor, AdminDoctor)


class AdminDoctorSummary(admin.ModelAdmin):
    search_fields = ("doctor",)
    list_display = ("doctor",)
    list_display_links = ("doctor",)


admin.site.register(DoctorSummary, AdminDoctorSummary)


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


class AdminDocumentCreator(admin.ModelAdmin):
    search_fields = (
        "document",
        "creator",
    )
    list_display = (
        "document",
        "creator",
    )
    list_display_links = (
        "document",
        "creator",
    )


admin.site.register(DocumentCreator, AdminDocumentCreator)
# End Docuemnt Models

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


# End Treatment History Models

# Start Appointments Models
class AdminAppointments(admin.ModelAdmin):
    list_display = (
        "doctor",
        "doctor_specialization",
        "patient",
        "date",
    )
    list_display_links = (
        "doctor",
        "doctor_specialization",
        "patient",
        "date",
    )
    search_fields = (
        "doctor",
        "doctor_specialization",
        "patient",
        "date",
    )


admin.site.register(Appointments, AdminAppointments)
# End Appointments Models
