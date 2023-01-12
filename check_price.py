#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is used as a debugging script to test the price scraping function

import requests
from datetime import date
import logging
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
    if price is None:
         raise ValueError('Price is None')
    else:
      return price

while True:
    try:
        price = define_price()
        break
    except NameError as e:
        logging.exception("An error occurred: %s", e)
        pass
    except ValueError as e:
        logging.exception("An error occurred: %s", e)
        pass
    finally:
        pass

print(price)