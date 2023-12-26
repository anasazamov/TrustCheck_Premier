from django.db import models


# Create your models here.

class Category(models.Model):

    pass


class Product(models.Model):

    name = models.CharField(max_length=30)
    product_hash = models.CharField(max_length=50,unique=True)
    product_seria_num = models.IntegerField()
    made_in = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    utilized = models.BooleanField(default=False)
    utilized_date = models.DateField(null=True)

    def __str__(self)->str:

        return f'Name: {self.name} ID: {self.pk}'