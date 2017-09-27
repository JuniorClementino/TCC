#!/usr/bin/python
#-*- coding: utf-8 -*-

from TwitterAPI import *
from datetime import *
from unicodedata import normalize
from pymongo import MongoClient



import sys
import json
import os.path  	
import time
import pymongo

def remover_acentos(tags_trend):
	for key, tag in enumerate(tags_trend):
		tags_trend[key] =normalize('NFKD', tag).encode('ASCII','ignore').decode('ASCII')

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


result_max = 100000
result_cont = 0
dh = datetime.now()
contador = 0
tags_trend = []





r = twitter.request('trends/place', {'id': '23424768'})
for item in r.get_iterator():
	tweet = item['name']
	if contador<10:
		print(tweet)
		tags_trend.append(tweet)

		contador +=1
	else:{"Finalizado"}

	#w = twitter.request('search/tweets', {'q': item[item_cont]})

remover_acentos(tags_trend)
print(tags_trend)
#print('Coleta Relalizada com Sucesso! \n')



while result_cont < result_max:
	#print('Buscando...\n')
	#print('Isso Pode Demorar Um Pouco..\n')
	tag_cont = 0
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
				#print(type(inst))
				pass
		
		tag_cont += 1
			
		
		
		print("%d tweets capturados"%result_cont)