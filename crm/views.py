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

        return Response({'token': token.key})


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

        if not user:
            return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        name = data.get("name")
        made_in = data.get("made_in")
        description = data.get("description")
        end_date = data.get("end_date")
        product_seria_num = data.get("product_seria_num")

        try:
            product_count = Product.objects.count()
            product_hash = sha256_hash(sha256_hash(str(product_count + 1).encode('utf-8')))

            with transaction.atomic():
                product = Product.objects.create(
                    name=name,
                    made_in=made_in,
                    description=description,
                    product_hash=product_hash,
                    product_seria_num=product_seria_num,
                    end_date=end_date
                )

                create_product = CreateProduct.objects.create(user=user, product=product)

            serializer = ProductSerializerForAdmin(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        return Response({"message":"product has been deleted","product":serializer.data}, status=status.HTTP_204_NO_CONTENT)


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