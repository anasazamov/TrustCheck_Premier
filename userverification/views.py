from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import UserProfile
from random import randint
from time import sleep


class SendOTPAPI(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user_profile, created = UserProfile.objects.get_or_create(phone_number=phone_number)

        otp_secret = randint(100000,999999)
        if created:
            # Foydalanuvchi yangi yaratildi, OTP kodi o'rnatiladi
            
            user_profile.otp_secret = otp_secret
            user_profile.save()

        
        otp_code = otp_secret

        # OTP kodi yuborish loyihasi (masalan, SMS yoki email orqali yuborish)

        return Response({'message': f'OTP kodi muvaffaqiyatli yuborildi: {otp_code}'}, status=status.HTTP_200_OK)


class VerifyOTPAPI(APIView):
    def post(self, request):



        phone_number = request.data.get('phone_number')
        otp_code: str = request.data.get('otp_code')
        if otp_code.isalnum:
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
        print(otp_code,":",generated_code)
        if otp_code == generated_code:
            user_profile.otp_secret = ""
            # Tasdiqlash kodlari mos keladi
            token, created = Token.objects.get_or_create(user=user_profile)  # Token yaratish yoki olish
            user_profile.otp_secret = ""
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Tasdiqlash kodlari mos kelmaydi
            return Response({'message': 'Noto\'g\'ri OTP kod'}, status=status.HTTP_400_BAD_REQUEST)


