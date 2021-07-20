# pirkkabot 2.0

Pirkkabot innocently scans K-Ruoka webstore for Pirkka III -beer's price daily. 

To avoid getting caught on K-Ruoka bot blocker, pirkkabot is now containerized and mimics human user with Chrome engine. 

## Technologies used

- Docker
- Python
- Selenium WebDriver
- Tweepy

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
