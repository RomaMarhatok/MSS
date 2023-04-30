from django.contrib import admin
from .models import User, UserLocation, UserPersonalInfo


admin.site.site_header = "Панель админстрации MSS"
admin.site.site_title = "Панель админстрации MSS"
admin.site.index_title = "Панель админстрации MSS"
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
