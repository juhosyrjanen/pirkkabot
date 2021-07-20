#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
import tweepy
from secrets import *

#get today's pirkka price
with open('price_today', 'r') as file:
    price = file.read().replace('\n', '')

#date formating
date_today = date.today()
date_formated = date_today.strftime(' %d.%m.%Y ')

#twitter API auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#compose tweet and shoot
tweet = "Pirkka III-oluen hinta tänään"+ date_formated +"on " + price + "€."
print(tweet)
api.update_status(status=tweet)
