from flask import Flask, jsonify
import os
import requests
from bs4 import BeautifulSoup
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Add the stream handler to the logger
logger.addHandler(ch) 

cache = {}

def define_price():
    if 'price' in cache:
        return cache['price']
    else:
        response = requests.get(
              url='https://proxy.scrapeops.io/v1/',
              params={
                  'api_key': os.environ.get('API_KEY'),
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
            cache['price'] = price
            return price

while True:
    try:
        price = define_price()
        break
    except NameError as e:
        logger.exception("An error occurred: %s", e)
        pass
    except ValueError as e:
        logger.exception("An error occurred: %s", e)
        pass
    finally:
        pass

try:
    price_float = float(price.text.replace(',','.'))
    logger.info('Price converted to float')
except ValueError:
    logger.error('Could not convert price to a float')

@app.route('/api/price', methods=['GET'])
def get_price():
    return jsonify({'price': price_float})

if __name__ == '__main__':
    app.run(debug=True)