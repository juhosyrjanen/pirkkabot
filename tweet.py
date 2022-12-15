#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
import tweepy
from secrets import *
import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriver options, headless, window size, user agent
# Make sure to update user agent regurarly
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

# Set up webdriver
driver = webdriver.Chrome(options=options)
driver.get('https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260')   

# Parse Pirkka III-beer price from page source 
# Catch error if price is not found
try:
    price = driver.find_element(By.CLASS_NAME,'price')
except:
    print('Price not found')
    driver.quit()
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
print(tweet)

# Catch error if Tweet is unsuccessful
try:
   print("tweet")
   api.update_status(status=tweet)
except:
    print('Tweet not sent')
    driver.quit()
    exit()

# Close the driver
driver.quit()

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
