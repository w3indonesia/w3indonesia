from django.contrib import admin
from .models import Scholarship

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('provider', 'location', 'application_deadline', 'views', 'posted_at')
    list_filter = ('location', 'application_deadline', 'grade_s1_status', 'grade_s2_status', 'grade_s3_status')
    search_fields = ('provider', 'description', 'eligibility', 'location')
    prepopulated_fields = {'slug': ('provider',)}  # Automatically fill slug based on provider
    readonly_fields = ('views', 'posted_at')  # Prevent edits to these fields in admin
    ordering = ('-posted_at',)  # Default ordering in admin

admin.site.register(Scholarship, ScholarshipAdmin)
