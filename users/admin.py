from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from users.custom_admin import custom_admin_site

@admin.register(User, site=custom_admin_site)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ['user_name', 'email', 'number', 'is_staff']
    search_fields = ['email', 'user_name']
    ordering = ['user_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('user_name', 'number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'number', 'password1', 'password2'),
        }),
    )
