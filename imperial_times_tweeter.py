'''
+++++++++The Imperial Times+++++++++
A Twitter bot created to generate simple news headlines from the warhammer 40k universe
This script is to tweet news made from the imperial_times_news.py file
'''

# Importing needed modules, tweepy for twitter api, time for delays, os for keys and news for news
import tweepy
import time
import os
import imperial_times_news

# Getting API keys from the Heroku environ
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# A cheeky while loop do the tweets
while True:
    tweet = str(imperial_times_news.tweet_news() + " #warhammer40k")
    api.update_status(status=tweet)
    print(tweet)
    time.sleep(18000)
