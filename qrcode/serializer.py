from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    utilized_date = serializers.DateField()
    class Meta:

        model = Product
        fields = "__all__"

class ProductSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
