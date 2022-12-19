# pirkkabot
> Reporting the important things to the masses

![pirkka-kun](pirkkabot.png)

Pirkkabot innocently scans K-Ruoka webstore for Pirkka III -beer's price daily (Kesko pls don't block, 1 page load per day only!).

## Technologies used

- Python
- Tweepy
- SQLite3

# Run Pirkkabot

To run Pirkkabot, populate secrets, run:

```shell
cd pirkkabot
mkdir db && touch db/pirkka_price.db
python3 ./tweet.py
```

### PirkkaDB

As of v1.0.1 Pirkka III-Olut daily price is saved to an SQLite database.
Database backups are handled at the server backend to the off-site NAS server.
