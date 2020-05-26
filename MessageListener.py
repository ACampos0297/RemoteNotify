#Author: Abdul Campos

#from ScreenNotification import ScreenNotification
import time
import tweepy
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    consumer_key = config["keys"]["consumer_key"]
    consumer_secret = config["keys"]["consumer_secret"]

    access_token = config["keys"]["access_token"]
    access_token_secret = config["keys"]["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    timeline = api.user_timeline()

    for tweet in timeline:
        print(tweet.text)

if __name__ == "__main__":
    main()
