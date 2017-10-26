#!/usr/bin/python
#-*- coding: utf-8 -*-

from TwitterAPI import *
from datetime import *
from unicodedata import normalize
from pymongo import MongoClient
from TwitterAPI import *
from datetime import *
from unicodedata import normalize
from pymongo import MongoClient
from datetime import datetime, date, time
import numpy as np
import pandas as pd
import os


import sys
import json
import os.path
import time
import pymongo



def remove_file():
	os.remove("TRENDS_TOP.csv")


def read_csv(file):
		df1 = pd.DataFrame.from_csv('%s.csv'%(file),sep=';',encoding ='ISO-8859-1')

		df1 = df1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')

		return df1



def remover_acentos(tags_trend):
	for key, tag in enumerate(tags_trend):
		tags_trend[key] =normalize('NFKD', tag).encode('ASCII','ignore').decode('ASCII')

def acents(text):
	return normalize('NFKD',text).encode('ASCII','ignore').decode('ASCII')

#Credencias de acesso App Twitter

consumer_key = "iSTl8Phe1eAaXuZPuOLi2iXTI"
consumer_secret = "XLG7yZWUfXgel5oF64ZB2RbIzA5nQlBQRQ4jMCZQDaTzy93Qy8"
access_token = "268551056-Fp5ya4TB5E5KRuQE4UJLT8pyVdpINdW4ztRuyKlC"
access_token_secret = "wlq5xEKhpveeUt0HRWX6zlJYwh7pgYq1btmn1wtwSYpw5"

#acessa OAuth
# Referencia para API: https://dev.twitter.com/rest/reference
twitter = TwitterAPI(consumer_key, consumer_secret,auth_type='oAuth2')


##DataBase

client = MongoClient()
db = client.baseTweetsTrends

tags_trend= []
result_max = 100000
result_cont = 0
dh = datetime.now()
contador = 0
 #Do arquivo para um array 
df = read_csv('TRENDS_TOP')
arr= df['tags'].values
print arr
tags_trend=arr


print(tags_trend)
remove_file()


#Adicionando os Trends no Banco de Dados




#Limpando o Arquivo, 





while result_cont < result_max:
	tag_cont = 0
	print('Buscando...\n')
	print('Isso Pode Demorar Um Pouco..\n')
	
	try:
		while tag_cont < len(tags_trend):
		
			r = twitter.request('search/tweets', {'q': tags_trend[tag_cont], 'lang':'pt-br','locale':'br', 'count':'10000'})
			for item in r.get_iterator():
				tweet1 = 'ID: %d, Usuario: %s, texto: %s, Horario: %s, Criado: %s \n'%(item['id'],item['user']['screen_name'],item['text'],dh.now(),item['created_at'])
				print(tweet1)
				try:
					db.tweets.insert_one(
						{
							'_id':item['id'],
							'id_user':item['user']['id'],
							'name':item['user']['screen_name'],
							'text':item['text'],
							'hourGet':dh.now(),
							'created_at':item['created_at'],
							'location':item['user']['location'],
							'retweets_count':item['retweet_count']
						}
					)

					result_cont += 1
				
				except Exception as inst:
					pass


			tag_cont += 1
					
				
		
			
			print("%d tweets capturados"%result_cont)		
	except Exception as	inst:
		print("OUTRO")
		print("AGUARDANDO TIME OUT")
		time.sleep(950)
		pass



		