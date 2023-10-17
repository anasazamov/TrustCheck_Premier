from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializer import ProductSerializer

class ProductView(APIView):
    def get(self,request, product_id):
        try:
            product = Product.objects.get(product_seria_num=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
class AllProductView(APIView):
    def get(self,request, product_id):
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, product_id):
        
        try:
            product = Product.objects.get(product_id)
            user = request.user
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        product.utilized = True
        serialazer = ProductSerializer(product)

        return Response(serialazer.data,status=status.HTTP_426_UPGRADE_REQUIRED)
        
        