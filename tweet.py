#v!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import date
import logging
import tweepy
from secrets import *
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

try:
    # Your code snippet goes here
    response = requests.get(
      url='https://proxy.scrapeops.io/v1/',
      params={
          'api_key': (api_key)',
          'url': 'https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260', 
          'render_js': 'true', 
          'residential': 'true', 
          'country': 'fi', 
      },
    )
except Exception as e:
    logging.exception("An error occurred: %s", e)


soup = BeautifulSoup(response.content, 'html.parser')

# Parse Pirkka III-beer price from page source 
# Catch error if price is not found
try:
    price = soup.find('span', class_='price')
    logging.info('Price found,' + price.text + '€')
except:
    logging.error('Price not found')
    exit()

# Transform price into float   
price_float = float(price.text.replace(',','.'))

# Get today's date and format it to day month year
date_today = date.today()
date_formated = date_today.strftime('%d.%m.%Y ')

# Twitter API auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
# Compose tweet and shoot
tweet = "Pirkka III-oluen hinta tänään "+ date_formated +"on " + price.text + "€."

# Catch error if Tweet is unsuccessful
try:
   api.update_status(status=tweet)
   logging.info('Tweet "' + tweet + '" sent.')
except:
    logging.error('Tweet not sent')
    exit()

## Database section ##
try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('db/pirkka_price.db')
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
