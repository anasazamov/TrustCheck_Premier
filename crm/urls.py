from django.urls import path
from .views import CreateProductAPI, UtilizedProduct, CreateProductTable, GetAllUser

urlpatterns = [
    path('create-product/', CreateProductAPI.as_view(), name='create-product'),
    path('create-product/<int:pk>/', CreateProductAPI.as_view(), name='get-update-delete-product'),
    path('utilized-product/', UtilizedProduct.as_view(), name='get-utilized-product'),
    path('create-product-table/', CreateProductTable.as_view(), name='get-create-product-table'),
    path('get-all-user/', GetAllUser.as_view(), name='get-all-user-table'),
]
