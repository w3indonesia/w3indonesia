from django.contrib import admin
from django import forms
from .models import Category, Project, Stage, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'slug', 'description')
    search_fields = ('name', 'description')
    ordering = ('order',)
    prepopulated_fields = {'slug': ('name',)}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'slug', 'description', 'requirements', 'final_product_description')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'requirements', 'final_product_description')
    ordering = ('order',)
    prepopulated_fields = {'slug': ('name',)}

class StageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'project', 'order', 'slug')  # Use __str__ method to show dynamic name
    list_filter = ('project',)
    search_fields = ('name',)
    ordering = ('order',)

    # We do not need prepopulated_fields here since `name` is not a direct field
    # Remove prepopulated_fields for Stage model

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'project', 'stage', 'status', 'order', 'created_at')
    list_filter = ('stage', 'status', 'stage__project__category')
    search_fields = ('title', 'content')
    ordering = ['order', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

    # Display category and project as readonly fields in the form

    # Override the form view to display these computed fields
    def get_readonly_fields(self, request, obj=None):
        """Dynamically set readonly fields."""
        readonly = super().get_readonly_fields(request, obj)
        if obj:  # When editing an existing object
            return readonly + ('category', 'project')
        return readonly

    def get_category_choices(self):
        return Category.objects.all()

    def get_project_choices(self):
        return Project.objects.all()






admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Article, ArticleAdmin)
