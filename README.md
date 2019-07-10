# pirkkabot
Posting the price of Pirkka III-beer daily

-- Installing --

pip install tweepy
needs lxml for python

-- How it works -- 

Fetch HTML-page from K-market webstore

Parse data for beer price tag

Turn parsed data into array

Use array[0] as variable 

Tweet string + variable

Scheduled cron jobs will trigger scripts daily

Not usefull at all, very simple

