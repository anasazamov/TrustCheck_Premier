from django.urls import path
from . import views

urlpatterns = [
    path('send-otp/', views.SendOTPAPI.as_view(), name='send-otp'),
    path('verify-otp/', views.VerifyOTPAPI.as_view(), name='verify-otp'),
    path('put-user/', views.UserProfilePut.as_view(), name='update-user'),
]
