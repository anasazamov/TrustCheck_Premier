from eskiz_sms import EskizSMS

def send_sms_func(phone_number, otp_code):

    email = "anasazamov55@gmail.com"
    password = "tB9hj59RqprOcqhKChkN2Cmg9W1pp2dMVbJ3ArZj"
    eskiz = EskizSMS(email=email, password=password)
    eskiz.send_sms(phone_number, f'TrustCheck Premierdan ro\'yxatdan o\'tish kodingiz {otp_code}', from_whom='TrusCheck Premier', callback_url=None)

    return eskiz