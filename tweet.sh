#!/bin/bash

docker run -it parser python3 ./parser.py > price_today
sleep 10
./tweet.py