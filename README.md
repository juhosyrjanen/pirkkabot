# pirkkabot
> Web scraper that avoids getting caught by Cloudflare. For now.

Pirkkabot innocently scans K-Ruoka webstore for Pirkka III -beer's price daily (Kesko pls don't block, 1 page load per day only!) To avoid getting caught on K-Ruoka bot blocker (AKA Cloudflare), pirkkabot is now containerized and mimics human user with Chrome engine. 

## Technologies used

- Docker
- Python
- Selenium WebDriver
- Tweepy
- SQLite3

## Chrome engine

To mimic human user, pirkkabot sets some additional args for WebDriver, such as window size and arbitary UA.

```python
options.add_argument("window-size=1920x1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")

```

Depending on the bot filter used, UA like this might be enough to circumvent the filter. Seems like requests coming from known datacenter IPs are more likely to get blocked, so UA DB might be needed eventually.

## Dockerfile

Docker image is based on ``python:3.7`` base image. It does not do much else than install Google Chrome and ``chromedriver`` which are used as a base for the webscraper. ``pip`` installs necessary Python-modules to support the parser. 

The container is only booted up once per day. ``parser.py`` is ran inside the container as ``pirkkabot`` user and its ``stdout`` is saved to a local file. 

```bash 
docker run parser > price_today
```

### PirkkaDB

As of v1.0.1 Pirkka III-Olut daily price is saved to an SQLite database. 
Database backups are handled at server backend to off-site NAS server.
