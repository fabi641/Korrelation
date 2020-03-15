#Hier wird der Tweet gebaut aus dem inhalt, der von korrelation.py erzeugt wird

import korrelation

#Twitter Kram
import twitter
import keys
api = twitter.Api(consumer_key=keys.consumer_key,
                  consumer_secret=keys.consumer_secret,
                  access_token_key=keys.access_token_key,
                  access_token_secret=keys.access_token_secret)


def tweet(picUrl, status, website):
    api.PostUpdate(status+"\n"+website, media = picUrl)
