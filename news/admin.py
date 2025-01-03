from django.contrib import admin
from .models import Category, NewsArticle

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 
    prepopulated_fields = {"slug": ("name",)} 

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category', 'is_published', 'is_featured')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content', 'author')
    list_editable = ('is_published', 'is_featured') 
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsArticle, NewsArticleAdmin)
