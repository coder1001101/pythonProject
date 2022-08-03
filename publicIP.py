import requests, time
a=1
while (a < 5):
	ip = requests.get("https://api.ipify.org").text
	print(a, ") Your new public ip address is :  ", ip)
	ip2=requests.get("https://ipinfo.io").text
	print("Your public ip with deteles : ", ip2)
	a += 1
	time.sleep(3)