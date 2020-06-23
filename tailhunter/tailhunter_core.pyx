# -*- coding: utf-8 -*-

from requests import Session
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from time import sleep

class search:
	
	def __init__(self, wordlist_path, target):
		
		self.wordlist_path = wordlist_path
		self.target = target
		self.found = []
		
	def read(self):
		
		print ("loading file.....")
		sleep(1)
		file = open(self.wordlist_path, "r")
		data = file.read().split("\n")
		file.close()
			
		words = []

		for line in tqdm(data):

			if line != " " and line !="" and line != "\n":
				line = line.strip()
				if line[0] == "/" :
					line = line[1:]
					words.append(line)
				else:
					words.append(line)
		del data
		return list(set(words))
		
	def get(self, session, word):
		
		try:
			target = f"{self.target}/{word}" 
			S = session()
			response = S.get(url=target, timeout=4)
		
			if response.status_code == 200:
				a = (f"\033[32m[+] [200] : \033[0m{target}")
				print(a)
				self.found.append(a)
			elif response.status_code < 404:
				print (f"\033[33m[=] [{response.status_code}] : \033[0m{target}")
			else:
				print (f"\033[31m[--] [404] : \033[0m{target}")
				
		except Exception as e:
			print ("\033[31mwarning : unknown error!\033[0m")

	def run(self):
		
		try:
			with ThreadPoolExecutor(max_workers=20) as ex:
				words = self.read()
				ex.map(self.get, [Session] * len(words), words)
				ex.shutdown(wait=True)
				
				for i in self.found:
					print ("\nfounded active url:\n\n")
					print (i)
					
		except:
			print ("\033[31mwarning : workers failed to load\033[0m")