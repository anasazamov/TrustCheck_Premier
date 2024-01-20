from django.urls import path
from .views import ProductView,UserProductView,UserProductView2


urlpatterns = [
    path("<str:product_hash>", UserProductView.as_view()),
    path("", UserProductView.as_view()),
    path("id/<int:product_id>", UserProductView2.as_view()),
    path("products/<str:product_id>", ProductView.as_view()),
]