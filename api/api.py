from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_price():
    conn = sqlite3.connect('../db/pirkka_price.db')
    c = conn.cursor()
    c.execute("SELECT * FROM PIRKKA_PRICE ORDER BY TIMESTAMP DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result[0]

@app.route('/price', methods=['GET'])
def get_price():
    latest_price = get_latest_price()
    return jsonify({'price': latest_price})

if __name__ == '__main__':
    app.run(debug=True)