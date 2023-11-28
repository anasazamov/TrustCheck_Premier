from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.model import User
from crm.models import UtilzedProduct
from .models import Product
from .serializer import ProductSerializer

#Avtaritzatsiyadan o'tmagan user lar uchun 

class ProductView(APIView):
    def get(self,request, product_id):
        try:
            product = Product.objects.get(product_seria_num=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#Avtorizatsiya  
class UserProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, product_id=None):
        if product_id:
            try:
                user = request.user
                product = Product.objects.get(product_seria_num = product_id)            
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            if not product.utilized:
                product.utilized = True
                utilezed = UtilzedProduct(product=product,user=user)

            
            serializer = ProductSerializer(product)
            return Response(serializer.data,status=status.HTTP_200_OK)

    

        
        