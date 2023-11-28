from django.db import models
from qrcode.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from userverification.models import UserProfile

class Activity(models.Model):

    name = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=2,decimal_places=1)
    description = models.TextField()

class CreateProduct(models.Model):

    product = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

class UtilzedProduct(models.Model):

    product = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
