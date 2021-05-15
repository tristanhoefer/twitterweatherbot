import tweepy
import pyowm
import secretfiles
#twitter auth keys

consumer_key = secretfiles.consumer_key
consumer_secret= secretfiles.consumer_secret
key = secretfiles.key
secret = secretfiles.secret

def access_api(consumer_key, consumer_secret, key, secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    return api

def get_mentions(api):
    mentions = api.mentions_timeline()
    print(mentions[0].text.split(" ")[1])
    return mentions

def get_tweetid(mentions):
    tweetid = str(mentions[0].id)
    return tweetid

def get_username(mentions):
    username = mentions[0].user.screen_name
    return username

def get_city(mentions):
    city = mentions[0].text.split(" ")[1]
    return city

#print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
#print ("Max Temp. Currently ", temp['temp_max']) # get max tmp
#print ("Min Temp. Currently ", temp['temp_min']) # get min tmp>>

#mentions = api.mentions_timeline()
#print(mentions[0].text.split(" ")[1])


#for mention in mentions:
#tweetid = str(mentions[0].id)
#username = mentions[0].user.screen_name
#city = mentions[0].text.split(" ")[1]

def access_owmapi():
#access OWM api
    APIKEY= secretfiles.APIKEY                #your API Key here as string
    OpenWMap=pyowm.OWM(APIKEY)  
    print(OpenWMap)
    return OpenWMap                # Use API key to get data

def get_weather(OpenWMap, city):
    mgr = OpenWMap.weather_manager()
    Weather=mgr.weather_at_place(city)  # give where you need to see the weather
    Data=Weather.weather                 # get out data in the mentioned location
    return Data

def get_avgtemp(Data):
    temp = Data.temperature(unit='celsius')
    avg_temp = round(temp["temp"],1)
    return avg_temp

def get_maxtemp(Data):
    temp = Data.temperature(unit='celsius')
    max_temp = round(temp["temp_max"],1)
    return max_temp

def get_mintemp(Data):
    temp = Data.temperature(unit='celsius')
    min_temp = round(temp["temp_min"],1)
    return min_temp

#print(avg_temp)
#print(max_temp)
#print(min_temp)

def post_tweet(api):    #post a tweet
    mentions = get_mentions(api)
    OpenWMap = access_owmapi()
    city = get_city(mentions)
    data = get_weather(OpenWMap, city)
    api.update_status("@" + get_username(mentions) + " The current temperature in " + city + " is: " + str(get_avgtemp(data)) + 
    " C degree. The maximal temperature for today will be " + str(get_maxtemp(data)) + " C degree and the minimal temperature " + 
    str(get_mintemp(data)) + " C degree!" + " Regardless of the weather I hope you enjoy your day :)", in_reply_to_status_id = get_tweetid(mentions))


#post a tweet
#api.update_status("@" + username + " The current temperature in " + city + " is: " + str(avg_temp) + " C degree. The maximal temperature for today will be " + str(max_temp) + " C degree and the minimal temperature " + str(min_temp) + " C degree!" + " Regardless of the weather I hope you enjoy your day :)", in_reply_to_status_id =tweetid)