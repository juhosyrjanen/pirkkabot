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
    return price

while True:
    try:
        price = define_price()
        break
    except NameError:
        logging.exception("An error occurred: %s", e)
        pass
    finally:
        pass
