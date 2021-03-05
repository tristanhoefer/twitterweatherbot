import tweepy
import pyowm

#twitter auth keys
consumer_key = "psh1Byop2V2y1GtriImm6U7nD"

consumer_secret= "OMoVLHoEsfsK3Y3bVonVtlXV2qXmkUQxqQC0nDZRvRvRZtSi3E"

key = "1367817972216193025-Cq6DggUYyFrj4Yt4PuNcyJ33nUdjgS"

secret = "eTHxiY1RRvEC3XL0p9vVY2KlNCUMwSt5TLUnpkbVvr8Ol"

#access twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


#print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
#print ("Max Temp. Currently ", temp['temp_max']) # get max tmp
#print ("Min Temp. Currently ", temp['temp_min']) # get min tmp>>

api = tweepy.API(auth)

mentions = api.mentions_timeline()
print(mentions[0].text.split(" ")[1])


#or mention in mentions:
tweetid = str(mentions[0].id)
username = mentions[0].user.screen_name
city = mentions[0].text.split(" ")[1]

#access OWM api
APIKEY='be8aa1bd5b1242928bf5b17070a6d473'                  #your API Key here as string
OpenWMap=pyowm.OWM(APIKEY)  
print(OpenWMap)                # Use API key to get data
mgr = OpenWMap.weather_manager()
Weather=mgr.weather_at_place(city)  # give where you need to see the weather
Data=Weather.weather                 # get out data in the mentioned location


temp = Data.temperature(unit='celsius')
avg_temp = temp["temp"]
max_temp = temp["temp_max"]
min_temp = temp["temp_min"]

#post a tweet
api.update_status("@" + username + " The current temperature in " + city + " is: " + str(avg_temp) + " C degree. The maximal temperature for today will be " + str(max_temp) + " C degree and the minimal temperature " + str(min_temp) + " C degree!", in_reply_to_status_id =tweetid)