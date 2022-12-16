#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date
import tweepy
from secrets import *
import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

# WebDriver options, headless, window size, user agent
# Make sure to update user agent regurarly
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\path\to\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

# Set up webdriver
driver = webdriver.Chrome(options=options)
driver.get('https://www.k-ruoka.fi/kauppa/tuote/pirkka-iii-olut-033l-45-tlk-si-6410405091260')   

#Print driver source
print(driver.page_source)

# Parse Pirkka III-beer price from page source 
# Catch error if price is not found
#try:
#    price = driver.find_element(By.CLASS_NAME,'price')
#except:
#    print('Price not found')
#    driver.quit()
#    exit()
#
## Get today's date and format it to day month year
#date_today = date.today()
#date_formated = date_today.strftime('%d.%m.%Y ')
#
#tweet = "Pirkka III-oluen hinta tänään "+ date_formated +"on " + price.text + "€."
#print(tweet)