from django.urls import path
from .views import *

urlpatterns = [
    path('create-product/', CreateProductAPI.as_view(), name='create-product'),
    path('login/', Login.as_view(), name='Login'),
    path('create-product/<int:pk>', CreateProductAPI.as_view(), name='get-update-delete-product'),
    path('utilized-product', UtilizedProduct.as_view(), name='get-utilized-product'),
    path('create-product-table', CreateProductTable.as_view(), name='get-create-product-table'),
    path('get-all-user', GetAllUser.as_view(), name='get-all-user-table'),
    path('search-product', SearchProduct.as_view(), name='search-product'),
    path('search-create-product', SearchCreateProduct.as_view(), name='search-CreateProduct'),
    path('search-utilied-product', SearchUtilizedProduct.as_view(), name='search-UtilezedProduct'),
    path('search-user', SearchUser.as_view(), name='search-user'),
]
