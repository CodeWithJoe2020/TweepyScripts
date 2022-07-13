#Delete All tweets


import tweepy
import threading
import sys, traceback




API_KEY = ''
APIKEY_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''



auth = tweepy.OAuthHandler(API_KEY, APIKEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def run_deletion():
    def delete_tweet(api, status_id):
        try:
            api.destroy_status(status_id)
            print("Deleted tweet: ", status_id)
        except:
            print("Could not delete tweet: ", status_id)
    
    index = 0
    for tweet in tweepy.Cursor(api.user_timeline).items():
        try:
            t = threading.Thread(target=delete_tweet, args=(api, tweet.id))
            index += 1
            print("Running deletion number %s" % index)
            t.start()
        except:
            print(traceback.print_exception(*sys.exc_info()))
            print("Deletion could not start on tweet %s" % tweet.id)

def run_unlike():
    def unlike_tweet(api, status_id):
        try:
            api.destroy_favorite(status_id)
            print("Removed favorite: ", status_id)
        except:
            print("Could not unfavorite tweet: ", status_id)
    
    index = 0
    for tweet in tweepy.Cursor(api.favorites, id="cmk256").items():
        try:
            t = threading.Thread(target=unlike_tweet, args=(api, tweet.id))
            index += 1
            print("Running unlike number %s" % index)
            t.start()
        except:
            print(traceback.print_exception(*sys.exc_info()))
            print("Unfavorite could not start on tweet %s" % tweet.id)

run_deletion()
