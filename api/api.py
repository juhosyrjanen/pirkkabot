from flask import Flask, jsonify
from flask_caching import Cache
import logging
import sqlite3

app = Flask(__name__)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Add the stream handler to the logger
logger.addHandler(ch) 

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.memoize(timeout=86400)
def get_latest_price():
    # Connect to the database
    conn = sqlite3.connect('db/pirkka_price.db')
    c = conn.cursor()
    
    # Get the latest price
    c.execute("SELECT PRICE FROM PIRKKA_PRICE ORDER BY TIMESTAMP DESC LIMIT 1")
    latest_price = c.fetchone()[0]
    
    # Close the connection
    conn.close()
    if latest_price is None:
        raise ValueError('Price is None')
    else:
        logger.info('Price fetched')
        return latest_price
        
while True:
    try:
        price = get_latest_price()
        logger.info('Price received from define_price()')
        break
    except NameError as e:
        logger.exception("An error occurred: %s", e)
        pass
    except ValueError as e:
        logger.exception("An error occurred: %s", e)
        pass
    finally:
        pass

@app.route('/api/price', methods=['GET'])
def get_price():
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
    