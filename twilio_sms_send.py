import requests
def send_sms(phone_number, otp_code):
    """Sends the verification code to the user via SMS."""

    url = "https://api.textport.com/v1/messages/send"
    data = {"From": "Trust Check Premier","To": "998990751735","MessageText": "Sample message from TextPort SMS API"}
    header = {"Authorization": "Basic MS1vcVk0OUNFRzhzOldqTk1ya2t6ZnFLbnQwV2c1bVdk"}

    response = requests.post(url=url,data=data,headers=header)

    return response


print(send_sms(1,1).json)
    



