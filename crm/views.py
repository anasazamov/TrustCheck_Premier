from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializer import *
from md5_hash import md5_hash
from .models import *
from qrcode.models import Product

class CreateProduct(APIView):

    permission_classes = [SessionAuthentication, BasicAuthentication]

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
        
    def post(self,request: Request):

        try:
            user = request.user
            data = request.data
        except:
            return Response({"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)
        
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        product_seria_num = md5_hash(Product.objects.last())
        how_many = data.get("how_many")
        created_products = []
        
        for i in range(0,how_many):
            product = Product.objects.create(name=name,price=price,description=description,product_seria_num=product_seria_num)
            create_at = CreateProduct.objects.create(user=user,product=product)
            created_products.append(product)

        serializer = ProductSerializer(product,many=True)
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

    permission_classes = [SessionAuthentication, BasicAuthentication]

    def get(self,request: Request):

        utilized = UtilzedProduct.objects.all()
        serializer = UtilzedProductSerializer(utilized,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class CreateProductTable(APIView):

    permission_classes = [SessionAuthentication, BasicAuthentication]

    def get(self,request: Request):

        utilized = CreateProduct.objects.all()
        serializer = CreateProductSerializer(utilized,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
