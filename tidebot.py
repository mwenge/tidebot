import sys
import os
import tweepy
from twilio.rest import Client 
from credentials import *
from datetime import datetime, timedelta
import json


client = tweepy.Client(consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret)

# Change working directory to script directory
os.chdir(sys.path[0])
json_file = open('high_tides.json')
tides = json.load(json_file)

def createTweet():
    local = datetime.now()
    lookup = datetime.strftime(local, "%Y-%m-%d")
    if lookup not in tides:
        return ""
    tides_today = tides[lookup]

    new_tweet = "🏊\n"
    new_tweet += '\n'.join(tides_today)
    return new_tweet

msg = createTweet()
print(msg)

# Tweet
try:
    client.create_tweet(text=msg)
except:
    print("Didn't tweet")

