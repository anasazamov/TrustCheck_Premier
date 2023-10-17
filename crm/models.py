from django.db import models
from qrcode.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):

    name = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=2,decimal_places=1)
    description = models.TextField()

class NewUser(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()


class CreateProduct(models.Model):

    product = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

class UtilzedProduct(models.Model):

    product = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
