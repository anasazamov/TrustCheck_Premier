from django.urls import path
from .views import NewUserView


urlpatterns = [

    path("",NewUserView.as_view()),
]