#!/usr/bin/python3.6

import json
from lxml import html
import requests

f= open("price.txt","w+")

page = requests.get('https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260')
tree = html.fromstring(page.content)

jsonld = tree.xpath('//script[@id="product-json-ld"]/text()')[0]
data = json.loads(jsonld)

price = data[0]['offers']['price']
price = price.replace('.', ',')

print (price)
f.write(price)

f.close()
