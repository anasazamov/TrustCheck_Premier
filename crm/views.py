from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializer import ProductSerializer
import md5_hash
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
        
        for i in range(0,data["seria"]):
            pass