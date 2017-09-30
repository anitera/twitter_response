import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import datetime as dt
from datetime import datetime, timedelta
import time
import os
import sys
import codecs
import io
import re

def load_api():
    consumer_key = '9Pls4VOFjj8fPRNc5XLWXQbPF'
    consumer_secret = '8z4wjK5aJ9j1KQl5qxiskG5pL5hyutcbc45psahzEpuIrDFKVx'
    access_token = '854038913727516672-9Dt0RaINnUz0lLju6bV9pE7PVhxcAxB'
    access_secret = 'LlnU8ri5SWakSDpWmntWBoxCCJwhmsGvpi911FLy3Jg8H'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def tokenize(s):
		return tokens_re.findall(s)
	 
def preprocess(s, lowercase=False):
	tokens = tokenize(s)
	if lowercase:
		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	return tokens
	
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('data.json', 'w')
        super(MyStreamListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            #self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False


def datarun(tag):
	auth = load_api()
	myStream = tweepy.Stream(auth, listener=MyStreamListener(time_limit=420))
	myStream.filter(track=['#'+tag])

	ccode = "US"

	with codecs.open('data.json', 'r') as fin, open('data_filtered_test.txt', 'w') as fout:
		for line in fin:
			tweet = json.loads(line)
			if 'country_code' in tweet.keys() and 'retweet_count' in tweet.keys() and 'favorite_count' in tweet.keys():
					if tweet['lang'] == "en" and tweet['country_code'] == ccode and tweet['retweet_count'] > 0 and tweet['favorite_count'] > 0:
						#print tweet['text']
						fout.write(tweet['text'].encode('ascii', errors='backslashreplace'))
			else:
					if tweet['lang'] == "en":
						#print tweet['text']
						fout.write(tweet['text'].encode('ascii', errors='backslashreplace'))
	emoticons_str = r"""
		(?:
			[:=;] # Eyes
			[oO\-]? # Nose (optional)
			[D\)\]\(\]/\\OpP] # Mouth
		)"""
	 
	regex_str = [
		emoticons_str,
		r'<[^>]+>', # HTML tags
		r'(?:@[\w_]+)', # @-mentions
		r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
		r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs 
		r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
		r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
		r'(?:[\w_]+)', # other words
		r'(?:\S)' # anything else
	]
		
	tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
	emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
	 
	with open('data_filtered_test.txt', 'r') as fin, open('data_token.txt', 'w') as fout:
		for line in fin:
			tweet = line
			#print(preprocess(tweet))
			fout.write(tweet)