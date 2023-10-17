from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from qrcode.models import Product

# Create your views here.
class UserView(APIView):

    def get(self):
        pass
