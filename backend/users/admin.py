from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
#admin.site.register(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["user_name", "email", "number", "is_staff", "public_id"]

    search_fields = ["user_name", "email", "number"]

    fieldsets = (
        (
            (None, {"fields":("password",)})
        ),

        (
            ("Personal Info", {"fields": ("user_name", "email", "number")})
        ),

        (
            ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")})
        ),

        (
            ("Important Dates", {"fields": ("last_login",)})
        )
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':("user_name", "email", "number", "password1", "password2"),
        }),
    )

    ordering = ['user_name', 'email']