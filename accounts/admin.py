from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class UserNetAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_staff",
    )
    list_display_links = ("id", "username")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "phone")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            ("Important dates"),
            {"fields": ("last_login", "date_joined", "last_activity")},
        ),
    )
