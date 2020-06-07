# Author: Abdul Campos

#from ScreenNotification import ScreenNotification
import time
import tweepy
import configparser
import json

# Tweet is formatted as a Json dump and printed to screen
def debugTweet(tweet):
    print(json.dumps(tweet._json, indent=2))

def main():

    # API Initialization
    config = configparser.ConfigParser()
    config.read('settings.ini')

    consumer_key = config["keys"]["consumer_key"]
    consumer_secret = config["keys"]["consumer_secret"]

    access_token = config["keys"]["access_token"]
    access_token_secret = config["keys"]["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Used for making calls to the Twitter API using tweepy
    api = tweepy.API(auth)

    # Account we are getting tweets from
    twitterAccount = "FromAtoL1"

    # Get the first tweet from the specificed account
    tweet = api.user_timeline(twitterAccount, count=1)[0]
    print(tweet.favorite_count)
    print(tweet.text)

    # Check if tweet has been favorited by this account
    favorites = api.favorites() # Get all favorites for host account
    for favTweets in favorites:
        # If tweet id shows up in favorites then we have seen this tweet already
        if favTweets.id == tweet.id:
            print("Already liked")
            return 0

    api.create_favorite(tweet.id)


if __name__ == "__main__":
    main()
