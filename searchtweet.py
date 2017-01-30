# -*- coding:utf-8 -*-
import tweepy
import json
import time
from fileoutput import LocalFileOutput
from bloboutput import BlobStorageOutput

class TwitterClient:

    def __init__(self, api):
        self.__api = api
        self.__outObj = []

    def addOutput(self, obj):
        self.__outObj.append(obj)

    def getRawdata(self, query, count):
        if(count > 0):
            tweets = tweepy.Cursor(self.__api.search, q=query, lang='ja').items(count)
        else:
            tweets = tweepy.Cursor(self.__api.search, q=query, lang='ja').items()

        cnt = 0
        while True:
            try:
                tweet = next(tweets)
            except tweepy.TweepError:
                print("Hitting rate limit. Sleeping 15 min...")
                time.sleep(60 * 16)
                print("Re-starting...")
                continue
            except StopIteration:
                break

            for output in self.__outObj:
                print("[" + str(cnt) + "] Wrirting to " + output.__class__.__name__)
                text = json.dumps(tweet._json, sort_keys=True, ensure_ascii=False, indent=4)
                text = text + '\n'
                output.send(text)

            cnt += 1

        print("completed,  total tweets=" + str(cnt))
        return tweet

    def getSome(self, query, count):
        if(count > 0):
            tweets = tweepy.Cursor(self.__api.search, q=query, lang='ja').items(count)
        else:
            tweets = tweepy.Cursor(self.__api.search, q=query, lang='ja').items()

        cnt = 0
        while True:
            try:
                tweet = next(tweets)
            except tweepy.TweepError:
                print("Hitting rate limit. Sleeping 15 min...")
                time.sleep(60 * 16)
                print("Re-starting...")
                continue
            except StopIteration:
                break

            for output in self.__outObj:
                print("[" + str(cnt) + "] Wrirting to " + output.__class__.__name__)
                print("text: " + tweet.text)
                print("user name: " + tweet.user.name)
                print("screen name: " + tweet.user.screen_name)
                print("location: " + tweet.user.location)
                print("created at: " + str(tweet.created_at))
                print("RT: " + str(tweet.retweet_count))
                print("FAV: " + str(tweet.favorite_count))
                print("# of Folllowers: " + str(tweet.followers_count))
                print("Tweet ID: " + tweet.id_str)
                #text = json.dumps("created at: " + tweet.created_at, sort_keys=True, ensure_ascii=False, indent=4)
                #text = text + '\n'
                #output.send(text)

            cnt += 1

        print("completed,  total tweets=" + str(cnt))
        return tweet

def main():
    # Set oauth info for tweepy to be available
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

    fileName = 'tweet-20170111-azure.json'
    keywords = ['azure', '#Azure']
    query = ' OR '.join(keywords)
    print(query)

    tc = TwitterClient(api)
    fo = LocalFileOutput(fileName)
    tc.addOutput(fo)
    #blob = BlobStorageOutput('dataset',
            #'',
            #'',
            #fileName)
    #tc.addOutput(blob)
    tc.getSome(query, -1)

if __name__ == "__main__":
    main()
