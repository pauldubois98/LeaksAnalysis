import got3 as got
import sys

#max nb of tweets
n=0 #0 <=> all possibles

tweetCriteria = got.manager.TweetCriteria().setUsername('realDonaldTrump')\
                .setQuerySearch('leak').setMaxTweets(n)
#.setSince("2015-09-10")
for i in range(n):
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
    print(i, '-', tweet.text)
    print(tweet.date)
    print()

