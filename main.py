import config
import listener
import json
import tweepy
import requests
from tweepy import OAuthHandler
from tweepy import Stream

# set origin twitter accounts in this list. 
# To find out Twitter account IDs, you may use https://tweeterid.com/
twitter_accounts = [ "144405435",           # me
                    "3156511997",           # @CriptoNoticias
                    "1380641162445385733",  # @NoticiacriptoC
                    "3367334171",           # @BTCTN
                    "1151046460688887808",   # @BitcoinFear
                    ]

languages = ["en","es"] #<- set language es: spanish tweets; en: english tweets; ru: rusian tweets...

filter_level = 'low' #<- set filter level: "medium" or "low"

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.TOKEN, config.TOKEN_SECRET) 
    api = tweepy.API(auth)

    tweet = listener.StreamListener(config.API_KEY, config.API_SECRET, 
                                    config.TOKEN, config.TOKEN_SECRET)
    tweet.filter(follow=twitter_accounts,  
    languages=languages, filter_level=filter_level)









