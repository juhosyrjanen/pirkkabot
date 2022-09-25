# pirkkabot

> Reporting the important things to the masses

Pirkkabot innocently scans K-Ruoka webstore for Pirkka III -beer's price daily (Kesko pls don't block, 1 page load per day only!). As of release v2.0 Pirkkabot is utilising PirkkaAPI, ChromeEngine & Selenium are deprecated.

## Technologies used

- Good old Bash and RegEx.
- Docker
- Python
- Tweepy
- SQLite3

## Dockerfile

Docker image is based on ``python:3.7`` base image. 

# Run Pirkkabot

To run Pirkkabot, populate secrets and run:

```bash
docker run --mount type=bind,source="$(pwd)"/db,target=/app/db pirkkabot
```

### PirkkaDB

As of v1.0.1 Pirkka III-Olut daily price is saved to an SQLite database. 
Database backups are handled at server backend to off-site NAS server.
