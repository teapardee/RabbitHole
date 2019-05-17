import urllib.request
import json


name = input("Enter username: ")
key = 'AIzaSyA4zyuxHi6kaQ1p79FGdrTI-eEyeJWsQzQ'

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " had " + "{:,d}".format(int(subs)) + "subscribers!")