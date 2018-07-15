#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:22:13 2018

@author: rohanbagwe
"""
import sys
sys.path.append('../')
from mongo.mongo_conn import db
import pandas as pd
from pprint import pprint


'''
from pymongo import MongoClient
# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')

client = MongoClient('mongodb://rdbagwe:rdbagwe123@localhost:27017')
db = client.hotels_test
'''

db.authenticate('rdbagwe','rdbagwe123')

print(db)
cursor = db.hotels.find().limit(20) 

#for document in cursor: 
#    pprint(document)
df =  pd.DataFrame(list(cursor))
pprint(df)



db.hotels.insert_one(
        {
        "name": "test",
        "age": "test",
        "country": "test"
        })


for document in cursor: 
    pprint(document['name'])

for document in cursor: 
    pprint(document['address'])


db.logout()