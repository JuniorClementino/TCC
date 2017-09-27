#coletar dados do twitter utilizando o streaming com a api

import tweepy
import time
from datetime import datetime
import csv
from unicodedata import normalize
import pandas as pd
import nltk

#Credencias de acesso App Twitter
consumer_key = "NBL0CtVrn2ajbpaGEWC1GBY2c"
consumer_secret = "2F5Uz5VYg0ONu4xTYYZsWkAGfc3TYXCkXLCsXMJ1eCKOfhBTfS"
access_token = "2345718031-we2K2PETQXkz7NCexjdGuvE2L2rnd5KfouzN3Up"
access_token_secret = "aEQPKGifu1y29Wbh3u6Z0YIcjAsBC8VeD4Y75CDL2r12o"

#acessa OAuth
# Referencia para API: https://dev.twitter.com/rest/reference
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)

def write_file(datas,filename):
	with open('%s.csv'%(filename), 'a', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=';')
		for row in datas:
			spamwriter.writerow(row)

def write_dataframe(df,file):
    df.to_csv('%s.csv'%file, mode='a', sep=';',index=False, header=False)

def acents(text):
	return normalize('NFKD',text).encode('ASCII','ignore').decode('ASCII')
            
def clean(dataframe):
	new_df = []
	for df in dataframe:
		#expr = re.sub(r"http\S+", "", df)
		#expr = re.sub(r"@\S+","",expr)
		expr = acents(df)
		filtrado = [w for w in nltk.regexp_tokenize(expr.lower(),"\w+") if not w in nltk.corpus.stopwords.words('portuguese')]
		frase = ""
		for f in filtrado:
			frase += f + " "
		new_df.append(frase)

	return new_df


def get_tweets(tags):
    tweets = []
    day = []
    for tg in tags:
        results = api.search(q=tg)
        for r in results:
            #tweets.append(r['text'])
            tweets.append(r.text)
            day.append(datetime.now().strftime("%d-%m-%y"))
    
    return tweets,day

if __name__ == '__main__':


	tags = []
	line = []
	df = pd.DataFrame()
	trends = api.trends_place(23424768)
	data = trends[0]
	trend = data['trends']
	for item in trend:
		name = str(item['name'])
		name = acents(name)
		line  = (str(datetime.now()),name)
		tags.append(name)

	print(tags)
	df['tweets'], df['day'] = get_tweets(tags)
	#df['tweets'] = clean(df['tweets'])
	print(df)
	#write_file(line,'tags')