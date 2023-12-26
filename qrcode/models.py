from collections.abc import Iterable
from django.db import models
from md5_hash import sha256_hash


# Create your models here.

class Category(models.Model):

    pass


class Product(models.Model):

    name = models.CharField(max_length=30)
    product_hash = models.CharField(max_length=50)
    product_seria_num = models.IntegerField()
    made_in = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    utilized = models.BooleanField(default=False)
    utilized_date = models.DateField(null=True)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if not self.product_hash:
            self.product_hash = sha256_hash(Product.objects.last())
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self)->str:

        return f'Name: {self.name} ID: {self.pk}'