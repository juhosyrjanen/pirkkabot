#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import tweepy
from secret import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

with open('price.txt', 'r') as myfile:
   price=myfile.read().replace('\n', '')

tweet = "Pirkka III-oluen hinta tänään: " + price + "€."

api.update_status(status=tweet)

