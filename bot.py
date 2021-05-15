import tweepy
import pyowm
import apikeys
#twitter auth keys

def access_api(consumer_key, consumer_secret, key, secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    return api

def get_mentions(api):
    mentions = api.mentions_timeline()
    return mentions

def get_tweetid(mentions):
    tweetid = str(mentions[0].id)
    return tweetid

def get_username(mentions):
    username = mentions[0].user.screen_name
    return username

def get_city(mentions):
    if len(mentions[0].text.split(" ")) > 2:
        city = mentions[0].text.split(" ")[1] + " " + mentions[0].text.split(" ")[2]
    else:
        city = mentions[0].text.split(" ")[1]
    print(city)
    return city

def access_owmapi():
#access OWM api
    APIKEY= apikeys.APIKEY                #your API Key here as string
    OpenWMap=pyowm.OWM(APIKEY)  
    print(OpenWMap)
    return OpenWMap                # Use API key to get data

def get_weather(OpenWMap, city, api):
    try: 
        mgr = OpenWMap.weather_manager()
        Weather=mgr.weather_at_place(city)  # give where you need to see the weather
        Data=Weather.weather               # get out data in the mentioned location
        return Data
    except: #if the city in the tweet doesn't exists
        error_tweet("I don't know this city...are you sure you typed it correctly?:)", api)


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

def post_tweet(api):    #post a tweet
    mentions = get_mentions(api)
    OpenWMap = access_owmapi()
    city = get_city(mentions)
    data = get_weather(OpenWMap, city, api)
    if data == None: #if the city doesnt exist return directly (error tweet printed)
        return
    api.update_status("@" + get_username(mentions) + " The current temperature in " + city + " is: " + str(get_avgtemp(data)) + 
    " C degree. The maximal temperature for today will be " + str(get_maxtemp(data)) + " C degree and the minimal temperature " + 
    str(get_mintemp(data)) + " C degree!" + " Regardless of the weather I hope you enjoy your day :)", in_reply_to_status_id = get_tweetid(mentions))

def error_tweet(answer, api):
    mentions = get_mentions(api)
    api.update_status("@" + get_username(mentions) + " " + answer, in_reply_to_status_id = get_tweetid(mentions))



#post a tweet
#api.update_status("@" + username + " The current temperature in " + city + " is: " + str(avg_temp) + " C degree. The maximal temperature for today will be " + str(max_temp) + " C degree and the minimal temperature " + str(min_temp) + " C degree!" + " Regardless of the weather I hope you enjoy your day :)", in_reply_to_status_id =tweetid)