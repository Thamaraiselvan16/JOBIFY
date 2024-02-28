from django.contrib import admin
from .models import Industry, State, Job, ApplyJob

class ApplyJobInline(admin.StackedInline):
    model = ApplyJob
    extra = 1

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'city', 'state', 'salary', 'is_available', 'timestamp', 'industry', 'job_type')
    list_filter = ('is_available', 'industry', 'state', 'job_type')
    search_fields = ['job_title', 'company__company_name', 'city', 'industry__name', 'state__name', 'user__username']
    inlines = [ApplyJobInline]
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)

class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'timestamp', 'status')
    list_filter = ('status',)
    search_fields = ['user__username', 'job__job_title', 'status']
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Job, JobAdmin)
admin.site.register(ApplyJob, ApplyJobAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Industry, IndustryAdmin)
