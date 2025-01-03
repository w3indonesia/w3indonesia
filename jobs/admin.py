from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_at', 'expiration_date', 'salary', 'job_type', 'slug')
    search_fields = ('title', 'company', 'location', 'industry', 'job_type')
    list_filter = ('posted_at', 'job_type', 'industry', 'location')
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from the title field
    ordering = ['-posted_at']
    date_hierarchy = 'posted_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'company', 'location', 'industry', 'salary', 'job_type')
        }),
        ('Job Details', {
            'fields': ('qualifications', 'description', 'benefits', 'job_level', 'work_schedule')
        }),
        ('Additional Info', {
            'fields': ('company_logo', 'posted_at', 'expiration_date', 'apply_link', 'apply_email')
        }),
    )
    readonly_fields = ('posted_at',)  # Make 'posted_at' field read-only in the admin

admin.site.register(Job, JobAdmin)
