#!/bin/bash

./parser.sh > price_today
sleep 2
python3 ./tweet.py
