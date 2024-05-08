# customauth/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "first_name", "last_name", "is_staff", "is_superuser"]
    ordering = ["email"]
    exclude = ["username"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),  # Required fields
        ("Personal Info", {"fields": ("first_name", "last_name")}),  # Additional fields
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),  # Permissions
        ("Important dates", {"fields": ("last_login", "date_joined")}),  # Date information
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),  # Fields for adding a new user
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
