FROM python:3.7

WORKDIR /app
COPY . .

RUN useradd pirkkabot -ms /bin/bash && chown -R pirkkabot:pirkkabot /app && chmod +x /app/*.py && chmod +x /app/pirkkabot.sh
USER pirkkabot
RUN mkdir -p /app/db

RUN pip3 install --no-cache-dir tweepy
ENTRYPOINT ./pirkkabot.sh 
