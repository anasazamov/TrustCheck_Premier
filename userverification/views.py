from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework import status

from .models import UserProfile
from .serializer import UserProfileSerializer
from random import randint


class SendOTPAPI(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user_profile, created = UserProfile.objects.get_or_create(phone_number=phone_number)

        otp_secret = randint(100000,999999)
        if created:
            # Foydalanuvchi yangi yaratildi, OTP kodi o'rnatiladi
            
            user_profile.otp_secret = otp_secret
            user_profile.save()

        else:
            # foydalnuvchi ro'yxatdan o'tgan bo'lsa yangi otp o'rnatish
            user_profile.otp_secret = otp_secret


        otp_code = otp_secret

        # OTP kodi yuborish loyihasi (masalan, SMS yoki email orqali yuborish)

        return Response({'message': f'OTP kodi muvaffaqiyatli yuborildi: {otp_code}'}, status=status.HTTP_200_OK)


class VerifyOTPAPI(APIView):

    def post(self, request):

        phone_number = request.data.get('phone_number')
        otp_code: str = request.data.get('otp_code')
        if otp_code.isalnum():
            otp_code = str(otp_code)

        # Ma'lumotlar bazasidan foydalanuvchini topamiz, telefon raqam orqali
        try:
            user_profile = UserProfile.objects.get(phone_number=phone_number)
        except UserProfile.DoesNotExist:
            return Response({'message': 'Noto\'g\'ri OTP kod yoki telefon raqam'})
        
        if not user_profile.otp_secret:
            return Response({'message': 'OTP kod vaqti tugadi'})

        # Tasdiqlash kodi yaratish
        totp = (user_profile.otp_secret)
        generated_code = totp

        if otp_code == generated_code:
            
            phone_number = user_profile.phone_number
            try:
                user = User.objects.create(username=phone_number,password="password")
            except Exception as e:
                return Response(UserProfileSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # Tasdiqlash kodlari mos keladi
            token, created = Token.objects.get_or_create(user=user)  # Token yaratish yoki olish
            user_profile.delete()
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        else:
            # Tasdiqlash kodlari mos kelmaydi
            return Response({'message': 'Noto\'g\'ri OTP kod'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfilePut(APIView):   
    
    permission_classes = [IsAuthenticated]

    def get(self,request:Request):

        try:
            user = request.user
        except User.DoesNotExist:
            return Response({"message":"Does not exist user"},status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = ""

    def put(self,request: Request):

        try:
            user: User = request.user
            data = request.data
        except ObjectDoesNotExist:
            return Response({"messaege":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
        if "first_name" in data.keys():  
            
            user.first_name = data["first_name"]
            user.save()
            serializer = UserProfileSerializer(user)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif "last_name" in data.keys():  
            
            user.last_name = data["last_name"]
            user.save()
            serializer = UserProfileSerializer(user)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif "phone_number" in data.keys():  
            
            user.phone_number = data["phone_number"]
            user.save()
            serializer = UserProfileSerializer(user)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif ["phone_number","first_name","last_name"] == data.keys():  
            
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.phone_number = data["phone_number"]
            user.save()
        serializer = UserProfileSerializer(user)

        return Response({serializer.data},status=status.HTTP_200_OK)
        
        # else:

        #     return Response()
