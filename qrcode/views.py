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
    pass
#     def get(self,request, product_id):
#         try:
#             product = Product.objects.get(product_hash=product_id)
#         except Product.DoesNotExist:
#             return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class UserProductView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request: Request, product_hash=False):

        if product_hash:
            try:
                user: User = request.user
                product = Product.objects.get(product_hash = product_hash)
            except Product.DoesNotExist:
                return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            is_new = False

            try:
                utilezed = UtilzedProduct.objects.get(product=product)
                is_there=True
            except UtilzedProduct.DoesNotExist:
                is_there=False

            if (not product.utilized) and (not is_there) :
                serializer_is_new = ProductSerializer(product).data
                is_new = True
                product.utilized = True
                product.utilized_date = timezone.now().date()
                product.save()
                utilezed = UtilzedProduct.objects.create(product=product,user=user)

            if is_new:
                serializer = serializer_is_new
            else:
                serializer = ProductSerializer(product).data
            return Response(serializer,status=status.HTTP_200_OK)

        else:
            try:
                user = request.user
            except:
                return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            utilized_allproduct: UtilzedProduct = UtilzedProduct.objects.filter(user=user)
            products = [i.product for i in utilized_allproduct]
            serializer = ProductSerializer(products,many=True)


            return Response(serializer.data,status=status.HTTP_200_OK)



class UserProductView2(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request: Request, product_id):

        try:
            user: User = request.user
            product = Product.objects.get(pk = product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

