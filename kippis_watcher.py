#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import logging
import config 
import time
from secrets import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name} - Twitter handle is {tweet.user.screen_name}")

            #api.update_status(
            #    status="@{tweet.user.name} Kippis!",
            #    in_reply_to_status_id=tweet.id,
            #)
    return new_since_id

def main():
    #tweepy auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    since_id = 1
    while True:
        since_id = check_mentions(api, ["kippis", "Kippis"], since_id)
        logger.info("Waiting...")
        time.sleep(30)

if __name__ == "__main__":
    main()
