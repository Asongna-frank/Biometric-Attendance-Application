from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from bioattend.models import Administrator  # Ensure this import is here

User = get_user_model()

class CustomAdminSite(AdminSite):
    site_header = _("Custom Admin")
    site_title = _("Admin Portal")
    index_title = _("Welcome to the Admin Portal")

    def has_permission(self, request):
        # Only allow access to users who are in the Administrator table
        if request.user.is_active and (
                request.user.is_superuser or Administrator.objects.filter(pk=request.user.pk).exists()):
            return True
        return False

custom_admin_site = CustomAdminSite(name='custom_admin')
