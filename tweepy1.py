import os
import tweepy as tw
import pandas as pd

consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# Post a tweet from Python
api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
# Your tweet has been posted!

# Define the search term and the date_since date as variables
search_words = "#wildfires"
date_since = "2018-11-16"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)


#tweets -- data type <tweepy.cursor.ItemIterator at 0x7fafc296e400>

# .Cursor() returns an object that you can iterate or loop over to access the data collected. Each item in the iterator has various attributes that you can access to get information about each tweet including:

# the text of the tweet
# who sent the tweet
# the date the tweet was sent


# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
    

#The above approach uses a standard for loop. A list comprehension provides an efficient way to collect object elements contained within an iterator as a list.

# Collect tweets through list comprehension
tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(5)

# Collect a list of tweets
[tweet.text for tweet in tweets]

#to remove all retweets as they will duplicate the data only, use filter condition as shown below
new_search = search_words + " -filter:retweets"


#now run the cursor again and using list comprehension

tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(5)

[tweet.text for tweet in tweets]


#other arguments for tweet

'''tweet.user.screen_name provides the user’s twitter handle associated with each tweet.
tweet.user.location provides the user’s provided location.
You can experiment with other items available within each tweet by typing tweet. and using the tab button to see all of the available attributes stored.
'''

tweets = tw.Cursor(api.search, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(5)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs

tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])
tweet_text
