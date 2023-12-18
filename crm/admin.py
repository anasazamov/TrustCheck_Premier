from django.contrib import admin
from .models import Activity, CreateProduct, UtilzedProduct
# Activity modeli
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'description')
    list_filter = ('discount',)
    search_fields = ('name', 'description')
    list_per_page = 20

# CreateProduct modeli
@admin.register(CreateProduct)
class CreateProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')
    list_filter = ('product',)
    search_fields = ('user__username', 'product__name')
    list_per_page = 20

# UtilizedProduct modeli
@admin.register(UtilzedProduct)
class UtilizedProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')
    list_filter = ('product',)
    search_fields = ('user__username', 'product__name')
    list_per_page = 20
