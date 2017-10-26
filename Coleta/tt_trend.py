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
from threading import Thread

verifica_h = False

data_dic={'Trends_Tags':[''],'Dia':['']}

df_data = pd.DataFrame()



def saveTrends(tag,date):
	try:
		db.trends.insert_one(
						{
							'tag':tag,
							'date':date
						}
					)
	except Exception as inst:
		pass 																			#FUNÇÔES

def write_file(datas,filename):
	with open('%s.csv'%(filename), 'w') as csvfile:	
		spamwriter = (csv.writer((csvfile))) 
		for row in datas:
			spamwriter.writerow(row)
			
def write_dataframe(df,file):
    df.to_csv('%s.csv'%file, mode='w', sep=';',index=False, header=True)

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


class Th(Thread):

                def __init__ (self, num):
                	Thread.__init__(self)
                	self.num = num

                def run(self):

                    oi= datetime.now()
                    print(oi)
                    hour = int(oi.hour)
                    minute = int(oi.minute)
                    if hour == 16 and minute == 23:
						verifica_h=True

      





def main():


	result_cont = 0
	contador = 0
	tags_trend = []
	nome_arquivo= "TRENDS_TOP"




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
					data_arq = str (date.today())
					#remover_acentos(tags_trend)
					tags_trend.append(trends)
					#saveTrends(trends,data_arq)

					
	   #  RENOVERRRR    RT   db.getCollection('tweets_copy').remove({'text':{$regex:'^RT'}})
					
					

					
			data_arq = str (date.today())		
			print(len(tags_trend))		
			print(tags_trend)
			data_arq = str (date.today())
			
			if(verifica_h==True):
				df_data ['tags'], df_data['dia'] = tags_trend , data_arq 
				write_dataframe(df_data,nome_arquivo)
				saveTrends(df_data,data_arq)
				verifica_h=False
			else:
				time.sleep(60)




					

		except Exception as err:
			print("entro")
			print(type(err))
			#data_arq = str (date.today())
			#df_data ['tags'], df_data['dia'] = tags_trend , data_arq 
			#write_dataframe(df_data,nome_arquivo)
			pass
			
			

		#print"ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
	
if __name__ == "__main__":
	verifica_h =False
	a = Th(1)
	a.start() 
	main()


		




