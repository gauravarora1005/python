#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[5]:


os.curdir


# In[8]:


os.chdir(r"D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST")


# In[9]:


os.curdir


# In[10]:


ls


# In[12]:


g01 = pd.read_csv(r'SA2/AUST/2016Census_G01_AUS_SA2.csv')


# In[13]:


g01.head()


# In[14]:


type(g01['SA2_MAINCODE_2016'])


# In[20]:


#SA2_maincode is integer type so string operations to work on them, we first need to change the datatype to str

g01['SA2_MAINCODE_2016'] = g01['SA2_MAINCODE_2016'].astype(str)


# In[23]:


#extracting first letter from code to create a state/territory

g01['State'] = g01['SA2_MAINCODE_2016'].str.slice(start=0, stop=1)


# In[24]:


g01.head()


# In[25]:


g01['SA2'] = g01['SA2_MAINCODE_2016'].str.slice(start=5)


# In[26]:


g01.head()


# In[27]:


cols = g01.columns.tolist()


# In[28]:


cols


# In[41]:


SA2_g01 = g01


# In[65]:


SA2_g01_1007 = SA2_g01[SA2_g01.SA2=='1007']


# In[68]:


SA2_g01_1007.head()


# In[67]:


SA2_g01_1007.groupby(['SA2'])['Tot_P_P'].agg('sum')


# In[43]:


SA2_g01.head()


# In[44]:


del g01


# In[46]:


#remove dataframe from memory using garbage collector

import gc
gc.collect()


# In[48]:


SA1_g01 = pd.read_csv(r'SA1/AUST/2016Census_G01_AUS_SA1.csv')


# In[49]:


SA1_g01.head()


# In[51]:


#SA1_7digitcode is integer type so string operations to work on them, we first need to change the datatype to str

SA1_g01['SA1_7DIGITCODE_2016'] = SA1_g01['SA1_7DIGITCODE_2016'].astype(str)


# In[52]:


#extracting first letter from code to create a state/territory

SA1_g01['State_territory'] = SA1_g01['SA1_7DIGITCODE_2016'].str.slice(start=0, stop=1)
SA1_g01['SA2_code'] = SA1_g01['SA1_7DIGITCODE_2016'].str.slice(start=1, stop=5)
SA1_g01['SA1_code'] = SA1_g01['SA1_7DIGITCODE_2016'].str.slice(start=5)


# In[53]:


SA1_g01.head()


# In[59]:


SA1_g01_1007 = SA1_g01[SA1_g01.SA2_code == '1007']


# In[60]:


SA1_g01_1007.head()


# In[61]:


SA1_g01_1007.groupby(['SA2_code'])['Tot_P_P'].agg('sum')


# In[18]:


lookup_file = pd.read_excel(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\Statistical Area Codes Explaination.xlsx')


# In[70]:


lookup_file.head()


# In[19]:


SA2_lookup_file = lookup_file[lookup_file.ASGS_Structure == 'SA2']


# In[20]:


SA2_lookup_file.head()


# In[21]:


SA2_lookup_file['Census_Code_2016'] = SA2_lookup_file['Census_Code_2016'].astype(str)


# In[22]:



SA2_lookup_file['State'] = SA2_lookup_file['Census_Code_2016'].str.slice(start=0, stop=1)
SA2_lookup_file['SA2_code'] = SA2_lookup_file['Census_Code_2016'].str.slice(start=5)


# In[23]:


SA2_lookup_file.head()


# In[24]:


SA2_lookup_file.to_csv(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\processed_SA2_codes.csv')


# In[78]:


final = pd.merge(SA1_g01, SA2_lookup_file, how = 'left', left_on= ['State_territory', 'SA2_code'], right_on=['State', 'SA2_code'])


# In[79]:


final.head()


# In[81]:


final


# In[82]:


final.to_csv(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\Mergedfile.csv')


# In[3]:


#code to 

import os
SA2_lookup_file = pd.read_csv(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\processed_SA2_codes.csv')
SA2_lookup_file['State'] = SA2_lookup_file['State'].astype(str)
SA2_lookup_file['SA2_code'] = SA2_lookup_file['SA2_code'].astype(str)
folder = os.listdir(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\AUST')
input_directory = r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\AUST\\'
output_directory = r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\Processed\\'
output_cols = ['SA1_7DIGITCODE_2016','State','SA2_code','SA1_code','Census_Name_2016']

i=1
for file in folder:
    if i<=len(folder):
        print(type(file))
        input_file = input_directory+file
        print(input_file)
        df = pd.read_csv(input_file)
        #print(df.head())
        df['SA1_7DIGITCODE_2016'] = df['SA1_7DIGITCODE_2016'].astype(str)
        df['State'] = df['SA1_7DIGITCODE_2016'].str.slice(start=0, stop=1)
        df['SA2_code'] = df['SA1_7DIGITCODE_2016'].str.slice(start=1, stop=5)
        df['SA1_code'] = df['SA1_7DIGITCODE_2016'].str.slice(start=5)
        print("Processing Completed")
        file_name = output_directory+"processed_"+file
        print(file_name)
        processed_df = pd.merge(df, SA2_lookup_file, how = 'left', left_on= ['State', 'SA2_code'], right_on=['State', 'SA2_code'])
        print("Merged")
        cols = list(processed_df)
        processed_col_list = ['SA1_7DIGITCODE_2016','State','SA2_code','SA1_code','Census_Name_2016']
        j = 0
        for name in processed_col_list:
            #ind = cols.index(name)
            cols.insert(j, cols.pop(cols.index(name)))
            j=j+1

        #print(cols)
        final_df = processed_df.ix[:, cols]
        print("Columns Reordered")

        #print(temp_df2.head())
        final_df.to_csv(file_name)
        i=i+1                  
print("Completed")

      


# In[ ]:





# In[ ]:





# In[4]:


#or we can use scandir method of os as below

directory = r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\AUST'
with os.scandir(directory) as files:
    for file in files:
        print(file.name)


# In[43]:


i = 1
#df = 
directory = r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\Processed\\'
for file in folder:
    if i <=2:
        #print(file,"_",i)
        df = file
        filename = "processed_"+df
        filename2 = directory+filename
        print(filename2)
        i=i+1
        #print(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\Processed/'+filename)


# In[37]:


os.listdir(directory)


# In[54]:


print(SA2_lookup_file['State'].dtype)


# In[57]:


temp_df = pd.read_csv(r'D:\Backup\IAG\Non Billable Work\Census\General Community Profile\2016 Census GCP All Geographies for AUST\SA1\Processed\processed_2016Census_G02_AUS_SA1.csv.csv')


# In[64]:


col_list = ['SA1_7DIGITCODE_2016','State','SA2_code','SA1_code','Census_Name_2016']

cols = list(temp_df)
i = 0
for name in col_list:
    #ind = cols.index(name)
    cols.insert(i, cols.pop(cols.index(name)))
    i=i+1

print(cols)
temp_df2 = temp_df.ix[:, cols]

print(temp_df2.head())


# In[ ]:




