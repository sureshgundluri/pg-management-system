from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Show these fields in admin list view
    list_display = ('username','email','role','is_staff','is_active')

    # Add role to fieldsets (for editing user in admin)
    fieldsets = UserAdmin.fieldsets+(
        (None,{'fields':('role',)}),
    )

    # Add role to add_fieldsets (when creating new user in admin)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(PG)
admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(Tenant_Profile)
