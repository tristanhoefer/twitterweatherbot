import tweepy
import pyowm

print("Hello World")

consumer_key = "psh1Byop2V2y1GtriImm6U7nD"

consumer_secret= "OMoVLHoEsfsK3Y3bVonVtlXV2qXmkUQxqQC0nDZRvRvRZtSi3E"

key = "1367817972216193025-Cq6DggUYyFrj4Yt4PuNcyJ33nUdjgS"

secret = "eTHxiY1RRvEC3XL0p9vVY2KlNCUMwSt5TLUnpkbVvr8Ol"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


APIKEY='32 bit hexadecimal'                  #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
Weather=OpenWMap.weather_at_place("London")  # give where you need to see the weather
Data=Weather.get_weather()                   # get out data in the mentioned location

api = tweepy.API(auth)
api.update_status("New Tweet")