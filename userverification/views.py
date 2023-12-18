from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializer import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework import status
from eskiz_sms_send import send_sms_func

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
        send_sms_func(phone_number,otp_code)
        return Response({'message': f'OTP kodi muvaffaqiyatli yuborildi'}, status=status.HTTP_200_OK)


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
        second = 3001
        if user_profile.get_time_difference() > second:
            user_profile.delete()
            return Response({'message': 'OTP kod vaqti tugadi'})

        # Tasdiqlash kodi yaratish
        totp = user_profile.otp_secret
        generated_code = totp

        if otp_code == generated_code:
    
            phone_number = user_profile.phone_number
            try:
                user,created = User.objects.get_or_create(username=phone_number,password=make_password("password"))
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
        
        serializer = UserSerializer(user)
        return Response(serializer.data,status.HTTP_200_OK)

    def put(self,request: Request):

        try:
            user: User = request.user
            data = request.data
        except ObjectDoesNotExist:
            return Response({"messaege":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
        
        #try:
        if "first_name" in data.keys() and len(data.keys()) == 1:  
            
            user.first_name = data["first_name"]
            user.save()
                
        elif "last_name" in data.keys() and len(data.keys()) == 1:  
                
            user.last_name = data["last_name"]
            user.save()
                        
        elif "first_name" in data.keys() and "last_name" in data.keys():  
                
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.save()

        elif "phone_number" in data.keys():
            otp = randint(100000,999999)
            update = UserProfile.objects.create(phone_number=data["phone_number"],otp_secret=otp)
            update.save()

            return Response({"message":f"Otp kod muvaqqiyatli yuborildi {otp}"})
        
        else:
            return Response({"message" : "Bad request"},status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request: Request):

        try:
            user = request.user
            data = request.data
            userprofile = UserProfile.objects.get(phone_number=data["phone_number"])
        except:
            return Response({"message":"Bad requeest"},status=status.HTTP_400_BAD_REQUEST)

        second = 301
        if userprofile.get_time_difference() > second:
            userprofile.delete()
            return Response({'message': 'OTP kod vaqti tugadi'})

        if userprofile.otp_secret == data["otp_code"]:
            user.username = data["phone_number"]
            user.save()
            userprofile.delete()
            serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response({"message":"otp_code mos kelmadi"},status=status.HTTP_400_BAD_REQUEST)
        
        
    
