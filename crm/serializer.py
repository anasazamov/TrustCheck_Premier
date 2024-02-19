from rest_framework import serializers
from django.contrib.auth.models import User
from qrcode.models import Product
from .models import *
from qrcode.serializer import ProductSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CreateProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Agar Product modeliga oid bo'lsa
    user = UserSerializer()
    class Meta:
        model = CreateProduct
        fields = ['id', 'product', 'user']

class UtilzedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Agar Product modeliga oid bo'lsa
    user = UserSerializer()

    class Meta:
        model = UtilzedProduct
        fields = ['id', 'product', 'user']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name"]