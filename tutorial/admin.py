from django.contrib import admin
from .models import Category, Subcategory, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'slug') 
    search_fields = ('name',)  
    ordering = ('order',) 
    prepopulated_fields = {'slug': ('name',)} 


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'slug')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('order',)
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'subcategory', 'order', 'slug', 'category')  
    list_filter = ('subcategory__category', 'subcategory', 'status')
    search_fields = ('title',)
    ordering = ('subcategory__order', 'order')
    prepopulated_fields = {'slug': ('title',)}  

    def category(self, obj):
        return obj.subcategory.category
    category.short_description = 'Category'
    category.admin_order_field = 'subcategory__category'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Article, ArticleAdmin)
