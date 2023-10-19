from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from qrcode.models import Product
from .serializer import NewUserSerialazer

# Create your views here.
class NewUserView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self,request: Request,pk=None):
        if pk:
            try:
                users = NewUser.objects.get(pk)
                serilizer = NewUserSerialazer(users)
            except NewUser.DoesNotExist:
                return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(serilizer.data,status=status.HTTP_200_OK)

        else:
            try:
                users = NewUser.objects.all()
                serilizer = NewUserSerialazer(users,many=True)
            except NewUser.DoesNotExist:
                return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(serilizer.data,status=status.HTTP_200_OK)

    def post(self,request: Request):
        
        serializer = NewUserSerialazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request: Request):
        pass