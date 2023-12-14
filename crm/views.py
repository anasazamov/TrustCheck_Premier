from msilib import datasizemask
from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db import transaction
from userverification.serializer import UserSerializer
from django.utils import timezone
from .serializer import *
from md5_hash import sha256_hash
from .models import *
from qrcode.models import Product

class CreateProductAPI(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request: Request, pk=False):

        if pk:
            try:
                product: Product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"message":"not found"},status=status.HTTP_200_OK)
            
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    @transaction.atomic
    def post(self, request: Request):
        try:
            user: User = request.user
            data = request.data
        except:
            return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)

        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        end_date = data.get("end_date")
        how_many = data.get("how_many")
        created_products = []

        # Generate serial numbers for all products outside the loop
        product_serial_numbers = [sha256_hash(str(i).encode('utf-8')) for i in range(Product.objects.count() + 1, Product.objects.count() + how_many + 1)]

        with transaction.atomic():
            products_to_create = [
                Product(
                    name=name,
                    price=price,
                    description=description,
                    product_seria_num=serial_number,
                    end_date=end_date
                )
                for serial_number in product_serial_numbers
            ]

            created_products = Product.objects.bulk_create(products_to_create)

            create_for_CreateProduct = [
                CreateProduct(user=user, product=product)
                for product in created_products
            ]

            CreateProduct.objects.bulk_create(create_for_CreateProduct)

        serializer = ProductSerializer(created_products, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
    def delete(self,request: Request,pk=False):

        if pk:
            product = Product.objects.get(id=pk)
            deleted = product.delete()
        else:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ProductSerializer(deleted)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    

class UtilizedProduct(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request: Request):

        utilized = UtilzedProduct.objects.all()
        serializer = UtilzedProductSerializer(utilized,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class CreateProductTable(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request: Request):

        utilized = CreateProduct.objects.all()
        serializer = CreateProductSerializer(utilized,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class GetAllUser(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self):

        user = User.objects.filter(username__startswith='+')
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)