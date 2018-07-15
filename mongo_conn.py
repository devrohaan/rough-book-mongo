#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:19:42 2018

@author: rohanbagwe
"""

from pymongo import MongoClient


# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.hotels_test

