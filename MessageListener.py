#Author: Abdul Campos

#from ScreenNotification import ScreenNotification
import time
import tweepy
import json

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    timeline = api.user_timeline()

    for tweet in timeline:
        print(tweet.text)



if __name__ == "__main__":
    main()
