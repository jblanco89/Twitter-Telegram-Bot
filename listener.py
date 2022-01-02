import json
import tweepy
import requests
from tweepy import OAuthHandler
from tweepy import Stream
import config

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET

TOKEN = config.TOKEN
TOKEN_SECRET = config.TOKEN_SECRET


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET) 
api = tweepy.API(auth)

try:
  api.verify_credentials()
  print(f'Authentication OK')
except:
  print(f'error during authentication')


def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True

def get_extended_tweet(status):       
  tweet = str(status.extended_tweet['full_text'] + '\n\n' +
  'https://twitter.com/twitter/statuses/'+status.id_str) # print original tweet
  return tweet


def get_tweet(status):
  tweet =  str(status.text + '\n\n' +
  'https://twitter.com/twitter/statuses/'+status.id_str)
  return tweet


def remove_special_chars(telegram_tweet, chars_to_remove):
  for char in chars_to_remove:
    telegram_tweet = telegram_tweet.replace(char,'')
  return telegram_tweet


special_chars = "#@&"



class StreamListener(tweepy.Stream):
  ENDPOINT = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
  TELEGRAM_BOT_API_KEY = config.TELEGRAM_BOT_API_KEY
  TELEGRAM_CHANNEL_ID = config.TELEGRAM_CHANNEL_ID
  def on_status(self, status):
    # status = api.get_status(id, tweet_mode="extended")
    if from_creator(status):
      if hasattr(status, 'extended_tweet'):
        try:
          tweet = get_extended_tweet(status)
          # remove special charts from original tweet before send it to Telegram
          # special chars will be # and @
          telegram_tweet = tweet
          telegram_message = remove_special_chars(telegram_tweet=telegram_tweet,chars_to_remove=special_chars)
          req = self.ENDPOINT.format(self.TELEGRAM_BOT_API_KEY,
                                    self.TELEGRAM_CHANNEL_ID,
                                    telegram_message)
          print(telegram_message)
          requests.get(req)
          with open('tweets.txt', 'a', encoding='utf-8') as f:
              f.write(tweet + '\n\n')
        except BaseException as e:
          print("Error on_data %s" % str(e))
        return True
      else:
        tweet = get_tweet(status)
        telegram_tweet = tweet
        telegram_message = remove_special_chars(telegram_tweet=telegram_tweet,chars_to_remove=special_chars)
        req = self.ENDPOINT.format(self.TELEGRAM_BOT_API_KEY,
                                    self.TELEGRAM_CHANNEL_ID,
                                    telegram_message)
        requests.get(req)

    return True

  def on_error(self, status_code):
    if status_code == 420:
        print("Error 420")
        #returning False in on_error disconnects the stream
    return False
  



 

