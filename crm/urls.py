from django.urls import path
from .views import CreateProduct, UtilizedProduct, CreateProductTable

urlpatterns = [
    path('create-product/', CreateProduct.as_view(), name='create-product'),
    path('create-product/<int:pk>/', CreateProduct.as_view(), name='get-update-delete-product'),
    path('utilized-product/', UtilizedProduct.as_view(), name='get-utilized-product'),
    path('create-product-table/', CreateProductTable.as_view(), name='get-create-product-table'),
]
