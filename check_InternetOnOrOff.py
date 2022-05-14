# if you chack internet is on or off 
# function 1
'''
import requests
url = 'https://google.com'
while True:
	try:
		request = requests.get(url, timeout=5)
		print('internet Connected')
	except:
		print('internet not Connected')
'''	
# function 2	
'''
import urllib
from urllib.request import urlopen
def int():
	try:
		urlopen('https://www.google.com',timeout=1)
		return True
	except urllib.error.URLError as error:
		print(error)
		return False
		
if int():
		print('active')
else:
		print('not active')
'''	
# funtion 3
import requests
import time
url = 'https://google.com'
while True:
	try:
		request = requests.get(url, timeout=5)
		if (request==True):
			print('internet Connected')
		else:
			time.sleep(5)
			print('not connected')
	except:
		time.sleep(5)
		print('internet not Connected')
		
