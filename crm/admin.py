from django.contrib import admin
from .models import Activity, CreateProduct, UtilzedProduct
# Activity modeli
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'description')
    list_filter = ('discount',)
    search_fields = ('name', 'description')

# CreateProduct modeli
@admin.register(CreateProduct)
class CreateProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')
    list_filter = ('product',)
    search_fields = ('user__username', 'product__name')

# UtilizedProduct modeli
@admin.register(UtilzedProduct)
class UtilizedProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')
    list_filter = ('product',)
    search_fields = ('user__username', 'product__name')
