from django.contrib import admin
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active', 'updated']
    list_filter =['price', 'active']
    list_editable = ['price', 'active']
    ordering = ['-updated']
    search_fields = ['title']
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
