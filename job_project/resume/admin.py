from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'location', 'job_title', 'upload_resume_display')
    search_fields = ['user__username', 'first_name', 'last_name', 'location', 'job_title']
    list_filter = ['experience', 'education']
    readonly_fields = ('upload_resume_display',)

    def upload_resume_display(self, obj):
        return obj.upload_resume.url if obj.upload_resume else None

    upload_resume_display.short_description = 'Resume URL'

admin.site.register(Resume, ResumeAdmin)
