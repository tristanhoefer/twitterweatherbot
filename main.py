import tweepy
import pyowm
import secretfiles
import bot

consumer_key = secretfiles.consumer_key
consumer_secret= secretfiles.consumer_secret
key = secretfiles.key
secret = secretfiles.secret

api = bot.access_api(consumer_key, consumer_secret, key, secret)

bot.post_tweet(api)