from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import transaction
from userverification.serializer import UserSerializer
from .serializer import *
from qrcode.serializer import ProductSerializerForAdmin
from md5_hash import sha256_hash
from .models import *
from django.db import transaction
from qrcode.models import Product

class Login(APIView):
    authentication_classes = [BasicAuthentication]


    def post(self,request: Request):

        user = request.user
        token,create = Token.objects.get_or_create(user=user)

        return Response({'token': token.key,'first_name':user.first_name,'last_name':user.last_name})


class CreateProductAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk=False):
        paginator = PageNumberPagination()
        paginator.page_size = 100
        if pk:
            try:
                product: Product = Product.objects.get(pk=pk)
                return Response(ProductSerializer(product).data,status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"message":"not found"},status=status.HTTP_200_OK)

            serializer = ProductSerializerForAdmin(product)
            return Response(serializer.data)

        else:
            products = Product.objects.all()
            result_page = paginator.paginate_queryset(products,request)
            serializer = ProductSerializerForAdmin(result_page,many=True)
            return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request: Request):

        user = request.user
        data = request.data

        name = data.get("name")
        made_in = data.get("made_in")
        description = data.get("description")
        end_date = data.get("end_date")
        from_ = data.get("from")
        up_to = data.get("up_to")
        ls = []

        product_count = Product.objects.count()
        while from_ <= up_to:

            product_hash = sha256_hash(sha256_hash(str(product_count + 1).encode('utf-8')))
            product = Product.objects.create(
                name=name,
                made_in=made_in,
                description=description,
                product_hash=product_hash,
                product_seria_num=from_,
                end_date=end_date
            )
            from_ += 1
            product_count += 1
            ls.append(product)
            CreateProduct.objects.create(user=user,product=product)

        serializer = ProductSerializerForAdmin(ls,many = True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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

        if "end_date" in data.keys():
            product.end_date = data.get("end_date")
        if "product_seria_num" in data.keys():
            product.product_seria_num = data.get("product_seria_num")
        if "made_in" in data.keys():
            product.made_in = data.get("made_in")
        product.save(force_insert=False,force_update=True)

        serializer = ProductSerializerForAdmin(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request: Request,pk=False):

        if pk:
            product = Product.objects.get(id=pk)
            deleted = product.delete()
        else:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(product)
        return Response({"message":204}, status=status.HTTP_204_NO_CONTENT)


class UtilizedProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request: Request):
        paginator = PageNumberPagination()
        paginator.page_size = 100
        utilized = UtilzedProduct.objects.all()
        result_page = paginator.paginate_queryset(utilized,request)
        serializer = UtilzedProductSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

class CreateProductTable(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request: Request):
        paginator = PageNumberPagination()
        paginator.page_size = 100
        created_product = CreateProduct.objects.all()
        result_page = paginator.paginate_queryset(created_product,request)
        serializer = CreateProductSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

class GetAllUser(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 100
        user = User.objects.filter(username__startswith='+')
        result_page = paginator.paginate_queryset(user,request)
        serializer = UserSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)

class SearchProduct(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request: Request):
        data = request.query_params

        if not data :
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        try:
            searched_produdct = Product.objects.filter(name__contains=data.get("name",""),product_seria_num__contains=data.get("product_seria_num",""),made_in__contains=data.get("made_in",""),id__contains = data.get("id",""))
        except Product.DoesNotExist:
            return Response({"message":"not found products"},status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializerForAdmin(searched_produdct,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SearchCreateProduct(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request: Request):
        data = request.query_params

        if not data:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        try:
            searched_produdct = Product.objects.filter(name__contains=data.get("name",""),product_seria_num__contains=data.get("product_seria_num",""),made_in__contains=data.get("made_in",""))
            user = User.objects.filter(username__contains=data.get("username",""),first_name__contains = data.get("first_name",""),last_name__contains=data.get("last_name",""))
        except Product.DoesNotExist:
            return Response({"message":"not found"},status=status.HTTP_404_NOT_FOUND)
        create_table = CreateProduct.objects.filter(user__in=user,product__in=searched_produdct)
        serializer = CreateProductSerializer(create_table,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SearchUtilizedProduct(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request: Request):
        data = request.query_params

        if not data:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        try:
            searched_produdct = Product.objects.filter(name__contains=data.get("name",""),product_seria_num__contains=data.get("product_seria_num",""),made_in__contains=data.get("made_in",""),pk__contains = data.get("id",""))
            user = User.objects.filter(username__contains=data.get("username",""),first_name__contains = data.get("first_name",""),last_name__contains=data.get("last_name"))
            create_table = UtilzedProduct.objects.filter(user__in=user,product__in=searched_produdct)
        except Product.DoesNotExist:
            return Response({"message":"not found"},status=status.HTTP_404_NOT_FOUND)

        serializer = CreateProductSerializer(create_table,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SearchUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request: Request):
        data = request.query_params

        if not data:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        try:
            searched_produdct = User.objects.filter(first_name__contains=data.get("first_name",""),last_name__contains=data.get("last_name",""),username__contains=data.get("phone_number",""),pk__contains = data.get("id",""))
        except Product.DoesNotExist:
            return Response({"message":"not found products"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(searched_produdct,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
