'''
+++++++++The Imperial Times+++++++++
A Twitter bot created to generate simple news headlines from the warhammer 40k universe
This script is to tweet news made from the imperial_times_news.py file
'''

# Importing needed modules, tweepy for twitter api, time for delays and news for news
import tweepy
import time
import imperial_times_news

# Creating variables for keys to pass to the API for authorisation
consumer_key = 'ctNkMPbduh6YSp7VCmKtbAocQ'
consumer_secret = 'qhAJ659GYj2m8hvCuoyIC8YMOT2BOXR6q0WopC1IThMgsolhsT'
access_token = '849994235940139016-meG7LZ1aWRSFIYkgLpHnUeQUoOOfLb3'
access_token_secret = 'i2CRdu8xxSC4Nkuc6pnnDYqSjxiu3eIwBjVmpIEOERyYu'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# A cheeky while loop do the tweets
while True:
    tweet = str(imperial_times_news.tweet_news())
    api.update_status(status=tweet)
    print(tweet)
    print('+++')
    time.sleep(120)
