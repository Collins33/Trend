import os
import tweepy
from time import sleep

# get the credentials
environment_key = os.environ
consumer_key = environment_key['CONSUMER_KEY']
consumer_secret = environment_key['CONSUMER_SECRET']
access_token = environment_key['ACCESS_TOKEN']
access_token_secret = environment_key['ACCESS_TOKEN_SECRET']

# authenticate our bot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# initialize the api
api = tweepy.API(auth)
# # wait on limit being set to true means the
# code will not crash when it reaches rate
# limit

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
