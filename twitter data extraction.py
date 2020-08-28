#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install advertools


# In[3]:


import pandas as pd
pd.set_option('display.max_colwidth', 60)
pd.set_option('display.max.columns', None) # 70+ columns to explore! 


# In[ ]:


# get these from your dashboard on developer.twitter.com: 
auth_params = {
    'app_key': 'YOUR_APP_KEY',
    'app_secret': 'YOUR_APP_SECRET',
    'oauth_token': 'YOUR_OAUTH_TOKEN',
    'oauth_token_secret': 'YOUR_OAUTH_TOKEN_SECRET',
}


# In[ ]:


# twython:
from twython import Twython
twitter = Twython(**auth_params) 
# twitter.search(q='basketball') 
# or any other function and / or parameters 

# advertools: 
import advertools as adv
adv.twitter.set_auth_params(**auth_params)
# adv.twitter.get_user_timeline(screen_name='twitter') 
# or some other function


# In[ ]:


##You can check what your auth params are for any function by calling adv.twitter.<function_name>.get_auth_params() and you will get a dictionary of the keys and parameters.


# In[ ]:


tweet_mode='extended'

#this is very very important to get the full text


# In[ ]:


# python = adv.twitter.search(q='#python', count=1000, tweet_mode='extended', lang='en')
# python.to_csv('python_tweets.csv', index=False) 


# In[ ]:


python = pd.read_csv('../input/python_tweets.csv', 
                     parse_dates=['tweet_created_at', 'user_created_at'])
print(python.shape)
python.head(3)


# In[ ]:


print('Columns starting with "tweet_" :', python.columns.str.contains('tweet_').sum()) 
print('Columns starting with "user_" :', python.columns.str.contains('user_').sum()) 


# In[ ]:


(python
 .sort_values(['user_followers_count'], ascending=False)
 [['tweet_full_text', 'user_screen_name', 
   'user_followers_count', 'user_description']]
 .head(10))

