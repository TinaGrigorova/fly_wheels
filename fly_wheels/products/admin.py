from django.contrib import admin
from .models import Product

admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'size', 'price')
    list_filter = ('category', 'brand', 'size')
    search_fields = ('name',)
