from rest_framework import serializers
from qrcode.models import Product
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CreateProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Agar Product modeliga oid bo'lsa
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = CreateProduct
        fields = ['id', 'product', 'user']

class UtilzedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Agar Product modeliga oid bo'lsa
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UtilzedProduct
        fields = ['id', 'product', 'user']


