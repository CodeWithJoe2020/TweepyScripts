#send tweets with current bitcoin price every hour


import tweepy
import time
import requests


API_KEY = ''
APIKEY_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#Authenticate
auth = tweepy.OAuth1UserHandler(
    API_KEY, APIKEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)



text = 'Bitcoin to the Moon 🚀\n#bitcoin #moon #btc #wgmi\n'




# Get Bitcoin price
def getPrice():
    url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    data = url.json()
    bitcoinPriceUsd = data['bitcoin']['usd']
    text2 = f'BTC Price: ${bitcoinPriceUsd:.2f} USD'
    #Tweet
    tweet = text + text2
    #send tweet
    api.update_status(tweet)
    


    
     




while True:
    try:
        getPrice()
        time.sleep(120)  #3600 
    except:
        pass
