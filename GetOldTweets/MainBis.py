import sys
import pandas as pd
import codecs
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import time

if sys.version_info[0] < 3:
import got
else:
import got3 as got

def main():

    def printTweet(descr, t):
	print(descr)
	print("Username: %s" % t.username)
	print("Retweets: %d" % t.retweets)
	print("Text: %s" % t.text)
	print("Mentions: %s" % t.mentions)
	print("Hashtags: %s\n" % t.hashtags)

    def receiveBuffer(tweets):
	for t in tweets:
	    outputFile.write(('\n%s;%s;%d;%d;"%s";%s;%s;%s;"%s";%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
	outputFile.flush()
	print('More %d saved on file...\n' % len(tweets))


    # keys_to_scrap = ["Montpellier", "Saurel_p", "Toulouse"]
    keys_to_scrap = ["levigan", "ganges"]

    start_date = date(2018, 01, 01)
    end_date = date(2018, 06, 01)
    daterange = pd.date_range(start_date, end_date)

    for key in keys_to_scrap:
	print("Collecting tweets by key : ", key)
	for single_date in daterange:
            day_plus = single_date + relativedelta(days=1)
            outputFilePath = "./"  + key + "/"
            outputFileName  = str(single_date.strftime("%Y-%m-%d")) + ".csv"

            if not os.path.exists(key):
                os.makedirs(key)


		print("Collecting tweets beetwin", single_date.strftime("%Y-%m-%d"), " to ", day_plus.strftime("%Y-%m-%d"), "for", outputFilePath + outputFileName)

		tweetCriteria = got.manager.TweetCriteria().setQuerySearch(key).setSince(single_date.strftime("%Y-%m-%d")).setUntil(day_plus.strftime("%Y-%m-%d"))
		tweet = got.manager.TweetManager.getTweets(tweetCriteria)
		time.sleep(2)

		outputFile = codecs.open(outputFilePath + outputFileName, "w+", "utf-8")
		outputFile.write('username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink')
		time.sleep(2)


		print('Searching...\n')



		got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
		time.sleep(2)

if name == 'main':
    main()
