from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'otp_secret')
    search_fields = ['phone_number']

admin.site.register(UserProfile, UserProfileAdmin)
