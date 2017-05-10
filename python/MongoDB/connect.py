import pymongo
from pymongo import *
client = MongoClient()
client = MongoClient("hostname", 27017)
client.mp_recom_stat.authenticate('user', 'passpord')

