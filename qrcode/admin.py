from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_seria_num', 'price', 'created', 'end_date', 'utilized')
    list_filter = ('created', 'end_date', 'utilized')
    search_fields = ('name', 'product_seria_num', 'description')
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
