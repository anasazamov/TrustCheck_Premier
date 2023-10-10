from django.urls import path
from .views import ProductView,AllProductView


urlpatterns = [
    path("<str:product_id>", ProductView.as_view()),
    path("products", AllProductView.as_view())
]