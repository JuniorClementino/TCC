from pymongo import MongoClient
import re 



regx = re.compile('^RT')

client = MongoClient()
db = client.baseTweetsTrends

db.tweets_copy.remove({'text':regx})