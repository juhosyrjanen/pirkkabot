#!/usr/bin/python3.6

import json
from lxml import html
import requests
from datetime import date
import tweepy
from secrets import *

f= open("price.txt","w+")

page = requests.get('https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260')
tree = html.fromstring(page.content)

#parse price
jsonld = tree.xpath('//script[@id="product-json-ld"]/text()')[0]
data = json.loads(jsonld)

#set price
price = data[0]['offers']['price']
price = price.replace('.', ',')

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