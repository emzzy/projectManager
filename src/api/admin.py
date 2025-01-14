from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Patient, MedicalProfessional, UserAccount


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'first_name', 'last_name', 'type')
    ordering = ('-email',)
    list_display = ('email', 'first_name', 'is_active', 'is_staff', 'type')


admin.site.register(UserAccount, UserAdminConfig)
admin.site.register(Patient)
admin.site.register(MedicalProfessional)