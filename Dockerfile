FROM python:3.10-slim

RUN pip3 install tweepy datetime selenium

WORKDIR /app
COPY . .

RUN useradd pirkkabot -ms /bin/bash && chown -R pirkkabot:pirkkabot /app && chmod +x /app/*.py 
USER pirkkabot
RUN mkdir -p /app/db

CMD python3 tweet.py