from django.db import models
from qrcode.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class NewUser(AbstractUser):
    # Oldin ishlatilayotgan bog'lanishlarni o'chiramiz
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='user_groups',
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='user_permissions',
        help_text=('Specific permissions for this user.'),
    )

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
