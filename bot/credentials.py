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
api = tweepy.API(auth, wait_on_rate_limit=True)
# wait on limit being set to true means the
# code will not crash when it reaches rate
# limit


# use a cursor to loop throught tweets
# and collect 50 tweets


# function to retweet tweets with specific word
def retweet(topic):
    for tweet in tweepy.Cursor(api.search, topic).items(2):
        try:
            # print(tweet.text)
            tweet.retweet()
            sleep(5)
        except Exception as e:
            print('could not complete task because of ', e)
        sleep(5)

# function to favourite a tweet


def favourite():
    for tweet in tweepy.Cursor(api.search, 'ambrose').items(2):
        try:
            print(tweet.text)
            tweet.favorite()
            sleep(5)
        except Exception as e:
            print('could not favorite because of ', e)
        sleep(5)

# function to follow a person


def follow():
    for tweet in tweepy.Cursor(api.search, 'wwe').items(2):
        try:
            user_name = tweet.author.screen_name
            print(user_name)
            api.create_friendship(user_name)
        except Exception as e:
            print('could not follow because of ', e)
        sleep(5)


# follow()
# favourite()
# retweet()

topic = raw_input("what topic do you want to retweet?")

retweet(topic)
