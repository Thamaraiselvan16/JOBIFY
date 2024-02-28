from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_recruiter', 'is_applicant', 'has_resume', 'has_company', 'is_active', 'date_joined')
    list_filter = ('is_recruiter', 'is_applicant', 'has_resume', 'has_company', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('User Type'), {'fields': ('is_recruiter', 'is_applicant', 'has_resume', 'has_company')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        (_('User Type'), {'fields': ('is_recruiter', 'is_applicant', 'has_resume', 'has_company')}),
    )

    readonly_fields = ('date_joined',)

admin.site.register(User, CustomUserAdmin)
