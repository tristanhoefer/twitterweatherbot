import tweepy
import pyowm


consumer_key = "psh1Byop2V2y1GtriImm6U7nD"

consumer_secret= "OMoVLHoEsfsK3Y3bVonVtlXV2qXmkUQxqQC0nDZRvRvRZtSi3E"

key = "1367817972216193025-Cq6DggUYyFrj4Yt4PuNcyJ33nUdjgS"

secret = "eTHxiY1RRvEC3XL0p9vVY2KlNCUMwSt5TLUnpkbVvr8Ol"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


APIKEY='be8aa1bd5b1242928bf5b17070a6d473'                  #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)  
print(OpenWMap)                # Use API key to get data
mgr = OpenWMap.weather_manager()
Weather=mgr.weather_at_place("London")  # give where you need to see the weather
Data=Weather.weather                 # get out data in the mentioned location

temp = Data.temperature(unit='celsius')
avg_temp = temp["temp"]
max_temp = temp["temp_max"]
min_temp = temp["temp_min"]
print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
print ("Max Temp. Currently ", temp['temp_max']) # get max tmp
print ("Min Temp. Currently ", temp['temp_min']) # get min tmp>>

api = tweepy.API(auth)
api.update_status("The current temperature in London is: " + str(avg_temp) + " degree. The maximal temperature for today will be " + str(max_temp) + " degree and a minimal temperature " + str(min_temp) + " degree")