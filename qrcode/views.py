from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils import timezone
from crm.models import UtilzedProduct
from .models import Product
from .serializer import ProductSerializer

class ProductView(APIView):
    def get(self,request, product_id):
        try:
            product = Product.objects.get(product_seria_num=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProductView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request: Request, product_id=None):
        pagiantor = PageNumberPagination()
        pagiantor.page_size = 20
        if product_id:
            try:
                user: User = request.user
                product = Product.objects.get(product_seria_num = product_id)            
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            is_new = False

            if not product.utilized:
                is_new = True
                serializer_is_new = ProductSerializer(product)
                product.utilized = True
                product.utilized_date = timezone.now()
                product.save()
                utilezed = UtilzedProduct.objects.create(product=product,user=user)

            if is_new:
                serializer = serializer_is_new
            else:
                serializer = ProductSerializer(product)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:
            try:
                user = request.user
                utilized_allproduct: UtilzedProduct = UtilzedProduct.objects.filter(user=user)
                products = [i.product for i in utilized_allproduct]
                result_page = pagiantor.paginate_queryset(products)
                serializer = ProductSerializer(result_page,many=True)
            except:
                return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(serializer.data,status=status.HTTP_200_OK)



    

        
        