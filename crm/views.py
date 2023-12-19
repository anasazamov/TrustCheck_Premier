from msilib import datasizemask
from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
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
        paginator = PageNumberPagination()
        paginator.page_size = 100
        if pk:
            try:
                product: Product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"message":"not found"},status=status.HTTP_200_OK)
            
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        else:
            products = Product.objects.all()
            result_page = paginator.paginate_queryset(products,request)
            serializer = ProductSerializer(result_page,many=True)
            return paginator.get_paginated_response(serializer.data)
        
    @transaction.atomic
    def post(self, request: Request):
        paginator = PageNumberPagination()
        paginator.page_size = 100
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
        product_serial_numbers = [sha256_hash(sha256_hash(sha256_hash(str(i).encode('utf-8')))) for i in range(Product.objects.count() + 1, Product.objects.count() + how_many + 1)]

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
        result_page = paginator.paginate_queryset(created_products,request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def put(self,request,pk):

        try:
            product = Product.objects.get(id=pk)
            data = request.data
        except Product.DoesNotExist:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        
        if "name" in data.keys():
            product.name = data.get("name")
        if "description" in data.keys():
            product.description = data.get("description")
        if "price" in data.keys():
            product.price = data.get("price")
        if "end_date" in data.keys():
            product.end_date = data.get("end_date")
        product.save()
        
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
        



        
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
        paginator = PageNumberPagination()
        paginator.page_size = 100
        utilized = UtilzedProduct.objects.all()
        result_page = paginator.paginate_queryset(utilized,request)
        serializer = UtilzedProductSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
    
class CreateProductTable(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request: Request):
        paginator = PageNumberPagination()
        paginator.page_size = 100
        created_product = CreateProduct.objects.all()
        result_page = paginator.paginate_queryset(created_product,request)
        serializer = CreateProductSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
    
class GetAllUser(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 100
        user = User.objects.filter(username__startswith='+')
        result_page = paginator.paginate_queryset(user,request)
        serializer = UserSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)