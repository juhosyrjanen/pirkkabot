#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import date
import logging
import tweepy
from secrets import *
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Add the stream handler to the logger
logger.addHandler(ch)

def define_price():
    response = requests.get(
          url='https://proxy.scrapeops.io/v1/',
          params={
              'api_key': 'API_KEY',
              'url': 'https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260', 
              'render_js': 'true', 
              'residential': 'true', 
              'country': 'fi', 
          },
        )
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find('span', class_='price')
    if price is None:
         raise ValueError('Price is None')
    else:
      return price

while True:
    try:
        price = define_price()
        break
    except NameError:
        logger.exception("An error occurred: %s", e)
        pass
    finally:
        pass

# Transform price into float for the database 
try:
    price_float = float(price.text.replace(',','.'))
    logger.info('Price converted to float')
except ValueError:
    logger.error('Could not convert price to a float')

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
   logger.info('Tweet "' + tweet + '" sent.')
except:
    logger.error('Tweet not sent')
    exit()

## Database section ##
try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('db/pirkka_price.db')
    cursor = sqliteConnection.cursor()
    logger.info('DB Init')

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
    logger.error('Error occured - ', error)

# Close the connection
finally:

    if sqliteConnection:
        sqliteConnection.close()
        logger.info('All good, SQLite Connection closed')
