#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
import tweepy
from secrets import *
import sqlite3
from sqlite3 import Error

#get today's pirkka price
with open('price_today') as price_raw:
    price = price_raw.readline().replace('\n', '').replace(',','.')
    price_float = float(price)

with open('price_today') as price_raw:
    price_totweet = price_raw.readline().replace('\n', '')

#date formating
date_today = date.today()
date_formated = date_today.strftime(' %d.%m.%Y ')

#twitter API auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#compose tweet and shoot
tweet = "Pirkka III-oluen hinta tänään"+ date_formated +"on " + price_totweet + "€."
print(tweet)
api.update_status(status=tweet)

## Database section ##

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('pirkka_price.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    ## Create Pirkka Price table
    pirkka_table = """ CREATE TABLE IF NOT EXISTS PIRKKA_PRICE (
                PRICE FLOAT,
                TIMESTAMP TEXT
            ); """

    cursor.execute(pirkka_table)
    cursor.execute(f"INSERT INTO PIRKKA_PRICE (PRICE, TIMESTAMP) VALUES ({price_float}, datetime('now'))")
    sqliteConnection.commit()
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print('Error occured - ', error)

# Close the connection
finally:

    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
