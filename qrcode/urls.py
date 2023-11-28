from django.urls import path
from .views import ProductView,UserProductView


urlpatterns = [
    path("<str:product_id>", UserProductView.as_view()),
    path("", UserProductView.as_view()),
    path("products<str:product_id>", ProductView.as_view()),
    #path("products", ProductView.as_view())
]