import tweepy
import pyowm
import apikeys
import bot

consumer_key = apikeys.consumer_key
consumer_secret= apikeys.consumer_secret
key = apikeys.key
secret = apikeys.secret

api = bot.access_api(consumer_key, consumer_secret, key, secret)

bot.post_tweet(api)