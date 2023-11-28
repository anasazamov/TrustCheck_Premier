from django.db import models
from django.utils import timezone



class UserProfile(models.Model):

    phone_number = models.CharField(max_length=15, unique=True)
    otp_secret = models.CharField(max_length=60)
    otp_expiration = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.phone_number}"

    def get_time_difference(self):

        current_time = timezone.now()
        created_time = self.otp_expiration
        time_difference = current_time - created_time
        seconds_difference = time_difference.total_seconds()

        return seconds_difference
