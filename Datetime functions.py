#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
time = dt.datetime.now()
datetime = dt.datetime.today()
dateonly = dt.datetime.now().strftime('%d-%m-%y')
datelong = dt.datetime.now().strftime('%d-%b-%Y')


'''strftime (i.e. string formatted time which results a string)
% d :1-31 %A : full weekday name : Sunday,Monday etc 
%m : 01-12 
%b : Jan-Dec 
%B : January, February etc 
%y = yy %Y = yyyy 
%H : hour 
%M : minute 
%S : seconds 
timedelta : kind of dateadd function'''


# In[3]:


fourWeeksLater = dt.datetime.today() + dt.timedelta(weeks = 4)

print(time)
#print(date)
print(dateonly)
print(datelong)

print(type(dateonly))


# In[ ]:




