#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
import requests,webbrowser

class Download:
	def __init__(self):
		self.R = '\033[1;31m'
		self.G ='\033[1;32m'
		self.w ='\033[1;39m'
		self.http = requests.Session()
		print(""" 
		
		
    ___                    _                 _        
   /   \_____      ___ __ | | ___   __ _  __| |       
  / /\ / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |       
 / /_// (_) \ V  V /| | | | | (_) | (_| | (_| |       
/___,' \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|       
                                                      
  _____           _                                   
  \_   \_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   
   / /\/ '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  
/\/ /_ | | | \__ \ || (_| | (_| | | | (_| | | | | | | 
\____/ |_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| 
                           |___/                      

		
		""")
		self.url=str(input(f"   {self.G}⌯ {self.w}Enter The Video Link From Instgram :"))
		self.info()		
	def info(self):
		if "reel" in self.url:
			self.cod =str(self.url)
			self.cipher=(self.cod[31:42])
			self.download_video()		
		elif "tv" in self.url:
			self.cod =str(self.url)
			self.cipher = (self.cod[29:40])			
			self.download_video()
		elif "p" in self.url:
			self.cod =str(self.url)
			self.cipher = (self.cod[28:39])			
			self.download_video()
			pass				
	def download_video(self):		
		self.req = self.http.get(f"https://www.instagram.com/p/{self.cipher}/?__a=1").json()["graphql"]["shortcode_media"]["video_url"]
		print("     ---------   ")
		print(f"   {self.G}⌯ {self.w}{self.req}  {self.G}⌯")		
		self.req = self.http.get(self.req).content		
		with open(f"ruks-download-video.mp4", 'wb') as f:
			f.write(self.req)	
			f.flush()
		webbrowser.open(self.url)

Download()	
