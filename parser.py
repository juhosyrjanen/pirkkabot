#!/usr/bin/python3.6

from lxml import html
import requests

f= open("price.txt","w+")

page = requests.get('https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260')
tree = html.fromstring(page.content)

price = tree.xpath('//span[@class="price"]/text()')
print (price[0])
f.write(price[0])

f.close()
