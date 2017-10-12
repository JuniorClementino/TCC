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

def read_csv(file):
		df1 = pd.DataFrame.from_csv('%s.csv'%(file),sep=',',encoding ='ISO-8859-1')

		df1 = df1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')

		return df1


df = read_csv('2017-10-12')

linha= df.shape
coluna = df.columns
index = df.index
count = df.count()

print df.head(30)


