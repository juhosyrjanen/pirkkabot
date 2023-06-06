# pirkkabot

> Reporting the important things to the masses

![pirkka-kun](pirkkabot.png)

Pirkkabot innocently scans K-Ruoka webstore for Pirkka III -beer's price daily. To combat ever changing CloudFlare and other bot blocking mechanisms used by K-Ruoka, Pirkkabot uses a combination of a managed distrubuted web scraper - [ScrapeOps](https://scrapeops.io/) and BeautifulSoup to scrape and parse K-Ruoka page contents.

!! Currently out of order, TwitterAPI1 has been deprecated. TwitterAPI2 requires some OAuth stuff and I'm a bit lazy. API still works! !!

## Technologies used

- Python
- Tweepy
- SQLite3
- BeautifulSoup :)
- ScrapeOps

## PirkkAPI

https://juho.tech/api/

`GET /pirkka_price`

Retrieve the latest price of Pirkka beer.
Returns

    200 OK on success with a JSON object containing the following property:
        price (float): latest price of the Pirkka-III beer in Euros.
    404 Not Found if the price is not found.

## PirkkaDB

As of v1.0.1 Pirkka III-Olut daily price is saved to an SQLite database.
Database backups are handled at the server backend to the off-site NAS server.

## Contributing

If you wish to contribute to Pirkkabot, please create a pull request with a description of your feature/bug fix.

Some things on the to do list are;

- Drawing graph on the price data
