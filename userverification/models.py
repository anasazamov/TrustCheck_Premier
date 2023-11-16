from django.db import models


class UserProfile(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    otp_secret = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"