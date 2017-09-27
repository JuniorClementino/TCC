#!/usr/bin/python
#-*- coding: utf-8 -*-

from TwitterAPI import *
from datetime import *
from unicodedata import normalize
from pymongo import MongoClient
from datetime import datetime, date, time



import sys
import csv
import json
import os.path  	
import time
import pymongo
import pandas as pd
df_data = pd.DataFrame()

 																			#FUNÇÔES

def write_file(datas,filename):
	with open('%s.csv'%(filename), 'a') as csvfile:
		spamwriter = (csv.writer((csvfile))) 
		for row in datas:
			spamwriter.writerow(row)
			
def write_dataframe(df,file):
    df.to_csv('%s.csv'%file, mode='a', sep=';',index=False, header=False)

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






result_cont = 0
contador = 0
tags_trend = []





  									#Coleta Streams intervalo de 1 minuto dos top 50 trends
while True:
	try:

		r = twitter.request('trends/place', {'id': '23424768'})
		for item in r.get_iterator():
			trends = item['name']
			print(trends)
			trends=acents(trends)
			#remover_acentos(tags_trend)
			if trends not in  tags_trend:
				#remover_acentos(tags_trend)
				tags_trend.append(trends)
				

				
				

				
		data_arq = str (date.today())		
		#df_data ['tags'], df_data['dia'] = tags_trend , data_arq 
		print(len(tags_trend))	
		#remover_acentos(tags_trend)			
		print(tags_trend)
		data_arq = str (date.today())
		#write_file(tags_trend, data_arq)
		#write_dataframe(df,data_arq)
		print df_data

		#write_dataframe(df_data,data_arq)
		datetime= datetime.now()
		print(datetime)

		hour = int(datetime.hour)
		minute = int(datetime.minute)

		print (hour)
		print(minute)
		if hour == 16 and minute == 45:
			print"oi"
			df_data ['tags'], df_data['dia'] = tags_trend , data_arq 
			write_dataframe(df_data,data_arq)



		time.sleep(58)
				

	except Exception as err:
		df_data ['tags'], df_data['dia'] = tags_trend , data_arq 
		write_dataframe(df_data,data_arq)

		#print"ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
	
	


#remover_acentos(tags_trend)
#print(tags_trend)
#print('Coleta Relalizada com Sucesso! \n')



		#	try:
				
		#	except Exception as inst:
			#	time.out(900)
			#	pass
		
	#	tag_cont += 1
			
		
		
		#print("%d tweets capturados"%result_cont)
