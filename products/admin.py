from django.contrib import admin
from .models import Product, Category, Creator


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'karat', 'creator']
    list_filter = ['category', 'karat', 'creator']
    search_fields = ['name']

    fieldsets = (
        ('Product Information', {
            'fields':
                ('sku', 'category', 'name', 'friendly_name', 'description',
                 'price', 'karat', 'creator')
        }),
        ('Image', {
            'fields': ('image',),
        }),
    )


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'friendly_name']
