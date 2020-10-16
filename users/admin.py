from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'fullname', 'prodi', 'status',)
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname', 'prodi', 'status', 'is_staff', 'password1', 'password2',)
        }),
    )

    list_display = ('created_on', 'email', 'fullname', 'status', 'prodi',)
    list_filter = ('status',)
    search_fields = ('email', 'fullname', 'prodi',)
    ordering = ('-created_on',)


admin.site.site_header = "DASHBOARD BENIH BELAJAR"
admin.site.register(models.CustomUser, UserAdmin)