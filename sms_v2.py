import requests

url = "https://messagebird-sms-gateway.p.rapidapi.com/sms"

querystring = {"username":"anasazamov55@gmail.com","password":"200024An#"}

payload = {
	"sender": "TrustCheck Premier",
	"body": "This is a gsm 7-bit test message.",
	"destination": "31600000001,31600000002",
	"reference": "268431687",
	"timestamp": "201308020025",
	"replacechars": "checked",
	"type": "normal",
	"dlr_url": "http://www.example.com/dlr-messagebird.php"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "6481c3e4d3mshdc90b0eb9744f02p1e145bjsn264c85d87aa9",
	"X-RapidAPI-Host": "messagebird-sms-gateway.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers, params=querystring)

print(response.json())