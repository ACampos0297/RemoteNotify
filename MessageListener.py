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
    timelineTweets = api.user_timeline(twitterAccount, count=1)
    
    tweetsAwaiting = ['']

    # Check if tweet has been favorited by any account more than once
    for tweet in timelineTweets:
        print(tweet.text)
        print("Favorite count")
        print(tweet.favorite_count)
        if tweet.favorite_count == 0: # Tweet has not been liked by any accounts
            print(tweet.text)
            tweetsAwaiting.append(tweet.text)
        else:
            print("Tweet liked")
            print(tweet.text)
    print(len(tweetsAwaiting))
    if len(tweetsAwaiting) == 0:
        print("No new tweets")
        return 0
    # Now that we have the tweets that haven't been shown to the user in tweetsAwaiting
    # go ahead and send notification that there is a new tweet awaiting and needs to be
    # displayed


    
if __name__ == "__main__":
    main()
