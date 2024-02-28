from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'rec_first_name', 'rec_last_name', 'company_contact_number', 'est_date', 'city', 'state', 'company_address', 'company_website', 'current_company_location')
    search_fields = ['company_name', 'rec_first_name', 'rec_last_name', 'city', 'state']

    fieldsets = (
        ('User Information', {
            'fields': ('user',),
        }),
        ('Company Details', {
            'fields': ('company_name', 'rec_first_name', 'rec_last_name', 'company_contact_number', 'est_date', 'city', 'state', 'company_address', 'company_website', 'current_company_location'),
        }),
    )

    readonly_fields = ('user',)

admin.site.register(Company, CompanyAdmin)
