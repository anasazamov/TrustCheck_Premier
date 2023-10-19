from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'otp_secret')
    search_fields = ('phone_number', 'last_name','first_name')

admin.site.register(UserProfile, UserProfileAdmin)
