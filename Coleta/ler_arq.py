from TwitterAPI import *
from datetime import *
from unicodedata import normalize
from pymongo import MongoClient
from datetime import datetime, date, time
import numpy as np




import sys
import csv
import json
import os.path
import time
import pymongo
import pandas as pd
tags_trend = []



def read_csv(file):
		df1 = pd.DataFrame.from_csv('%s.csv'%(file),sep=';',encoding ='ISO-8859-1')

		df1 = df1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')

		return df1

df = read_csv('2017-10-17')

#df = pd.read_csv('2017-10-17.csv', names= ['DIAS'])


linha= df.shape
coluna = df.columns
index = df.index
count = df.count()





#row = next(df.iterrows())[1]



arr= df['tags'].values
#str(arr)
#tags_trend.append(arr)
#print tags_trend

#oi= df['tags'].values[1]
#str(oi)
#tags_trend.append(oi)
#print tags_trend


numpy_teste=np.asarray(arr)
print numpy_teste






