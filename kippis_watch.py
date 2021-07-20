#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

twts = api.search(q="Kippis!")

#list of tweets pirkkabot responses to
t = ['kippis!',
    'kippis',
    'Kippis',
    'kippis!!',
    'Kippis!!',
    'kippis!!!',
    'Kippis!!!',
    'hölkynkölkyn!']

for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Kippis!" % (sn)
            s = api.update_status(m, s.id)