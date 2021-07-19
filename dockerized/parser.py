import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
import json

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260")
time.sleep(2)
src = driver.page_source
driver.close()
tree = html.fromstring(src)

jsonld = tree.xpath('//script[@id="product-json-ld"]/text()')[0]
data = json.loads(jsonld)

price = data[0]['offers']['price']
price = price.replace('.', ',')
print(price)
