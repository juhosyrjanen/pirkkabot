#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
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

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "Kippis @%s !" % (sn)
            s = api.update_status(m, s.id)