#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


os.chdir(r'D:\Backup\IAG\Non Billable Work\Census\Downloaded\LGA NSW\2016 Census GCP Local Government Areas for NSW')


# In[3]:


g05 = pd.read_csv('2016Census_G05_NSW_LGA.csv')


# In[4]:


g05.head()


# In[5]:


g01_cleaned = pd.read_csv(r'D:\Backup\IAG\Non Billable Work\Census\Data Prep\LGA NSW\g01_processed_v1.csv')


# In[6]:


g02_med_inc = pd.read_csv('2016Census_G02_NSW_LGA.csv')


# In[10]:


g01_cleaned.shape


# In[11]:


test = g02_med_inc.iloc[:,[0,3,5]]


# In[13]:


test.head(1)


# In[14]:


g01_02 = pd.merge(g01_cleaned, g02_med_inc.iloc[:,[0,3,5]], how='inner', on = 'LGA_CODE_2016')


# In[15]:


g01_02.shape


# In[17]:


g01_02.head()


# In[19]:


colnames = g01_02.columns.tolist()


# In[20]:


colnames


# In[50]:


g01_02['%young_males'] = ((g01_02['young_males'] * 100 ) / g01_02['Total_population']).round(2)
g01_02['%young_females'] = ((g01_02['young_females'] * 100 ) / g01_02['Total_population']).round(2)
g01_02['%young_population'] = ((g01_02['young_population'] * 100 ) / g01_02['Total_population']).round(2)

g01_02['%middle_age_males'] = ((g01_02['middle_age_males'] * 100 ) / g01_02['Total_population']).round(2)
g01_02['%middle_age_females'] = ((g01_02['middle_age_females'] * 100 ) / g01_02['Total_population']).round(2)
g01_02['%middle_age_population'] = ((g01_02['middle_age_population'] * 100 ) / g01_02['Total_population']).round(2)

g01_02['%old_age_males'] = ((g01_02['old_age_males'] * 100 ) / g01_02['Total_population']).round(2)
g01_02['%old_age_females'] = ((g01_02['old_age_females'] * 100 ) / g01_02['Total_population']).round(2)
g01_02['%old_age_population'] = ((g01_02['old_age_population'] * 100 ) / g01_02['Total_population']).round(2)


# In[22]:


g01_02.iloc[:,[1,2,26,-1]]


# In[24]:


g01_02.pop('%_young_males')


# In[51]:


g01_02.iloc[:,[1,2,4,26,-9,-8]]


# In[28]:


g01_02.shape


# In[40]:


g01_02.iloc[:,[1,2,26,-9]]


# In[47]:


g01_02['%young_males'].round(2)


# In[52]:


g01_02.to_csv('age_group_profiling.csv')


# In[ ]:




