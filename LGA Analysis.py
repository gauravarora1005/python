#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


os.chdir(r'D:\Backup\IAG\Non Billable Work\Census\Downloaded\LGA NSW\2016 Census GCP Local Government Areas for NSW')


# In[3]:


os.listdir()


# In[4]:


g01 = pd.read_csv('2016Census_G01_NSW_LGA.csv')


# In[7]:


g01.head(2)


# In[10]:


cols = g01.columns


# In[11]:


cols


# In[15]:


young_males = ['Age_0_4_yr_M','Age_5_14_yr_M','Age_15_19_yr_M']
young_females = ['Age_0_4_yr_F','Age_5_14_yr_F','Age_15_19_yr_F']

middle_age_males = ['Age_20_24_yr_M','Age_25_34_yr_M','Age_35_44_yr_M','Age_45_54_yr_M']
middle_age_females = ['Age_20_24_yr_F','Age_25_34_yr_F','Age_35_44_yr_F','Age_45_54_yr_F']

old_age_males = ['Age_55_64_yr_M','Age_65_74_yr_M','Age_75_84_yr_M','Age_85ov_M']
old_age_females = ['Age_55_64_yr_F','Age_65_74_yr_F','Age_75_84_yr_F','Age_85ov_F']


# In[16]:


type(young_males)


# In[19]:


g01['young_males'] = g01[young_males].sum(axis=1)


# In[22]:


g01.head()


# In[21]:


g01['young_females'] = g01[young_females].sum(axis=1)
g01['middle_age_males'] = g01[middle_age_males].sum(axis=1)
g01['middle_age_females'] = g01[middle_age_females].sum(axis=1)
g01['old_age_males'] = g01[old_age_males].sum(axis=1)
g01['old_age_females'] = g01[old_age_females].sum(axis=1)


# In[24]:


g01.drop(young_males, axis = 1, inplace= True)


# In[25]:


g01.head()


# In[26]:


g01.drop(young_females, axis = 1, inplace= True)
g01.drop(middle_age_males, axis = 1, inplace= True)
g01.drop(middle_age_females, axis = 1, inplace= True)
g01.drop(old_age_males, axis = 1, inplace= True)
g01.drop(old_age_females, axis = 1, inplace= True)


# In[27]:


g01.head()


# In[29]:


young_population = [s.replace('_M', '_P') for s in young_males]

middle_age_population = [s.replace('_M', '_P') for s in middle_age_males]
old_age_population = [s.replace('_M', '_P') for s in old_age_males]


# In[32]:


print(young_population)
print(middle_age_population)
print(old_age_population)


# In[33]:


g01['middle_age_population'] = g01[middle_age_population].sum(axis=1)
g01['young_population'] = g01[young_population].sum(axis=1)
g01['old_age_population'] = g01[old_age_population].sum(axis=1)


# In[34]:


g01.drop(middle_age_population, axis = 1, inplace= True)
g01.drop(young_population, axis = 1, inplace= True)
g01.drop(old_age_population, axis = 1, inplace= True)


# In[39]:


g01.head()


# In[54]:


remove_columns1 = ['Counted_on_Census_Night_At_home_Males','Counted_on_Census_Night_At_home_Females','Counted_on_Census_Night_At_home_Persons','Counted_on_Census_Night_Elsewhere_in_Australia_Males','Counted_on_Census_Night_Elsewhere_in_Australia_Females','Counted_on_Census_Night_Elsewhere_in_Australia_Persons','Aboriginal_and_or_Torres_Strait_Islander_Persons_Aboriginal_Males','Aboriginal_and_or_Torres_Strait_Islander_Persons_Aboriginal_Females','Aboriginal_and_or_Torres_Strait_Islander_Persons_Aboriginal_Persons','','Aboriginal_and_or_Torres_Strait_Islander_Persons_Torres_Strait_Islander_Males','Aboriginal_and_or_Torres_Strait_Islander_Persons_Torres_Strait_Islander_Females','Aboriginal_and_or_Torres_Strait_Islander_Persons_Torres_Strait_Islander_Persons','Aboriginal_and_or_Torres_Strait_Islander_Persons_Both_Aboriginal_and_Torres_Strait_Islander_Males','Aboriginal_and_or_Torres_Strait_Islander_Persons_Both_Aboriginal_and_Torres_Strait_Islander_Females','Aboriginal_and_or_Torres_Strait_Islander_Persons_Both_Aboriginal_and_Torres_Strait_Islander_Persons','Aboriginal_and_or_Torres_Strait_Islander_Persons_Total_Males','Aboriginal_and_or_Torres_Strait_Islander_Persons_Total_Females','Aboriginal_and_or_Torres_Strait_Islander_Persons_Total_Persons','Birthplace_Australia_Males','Birthplace_Australia_Females','Birthplace_Australia_Persons','Birthplace_Elsewhere_Males','Birthplace_Elsewhere_Females','Birthplace_Elsewhere_Persons']


# In[56]:


#for e in remove_columns1:
#        e = str(e).replace("\n", ',')


# In[61]:





# In[62]:


g01.head()


# In[75]:


remove_cols1 = g01.columns[g01.columns.str.contains(pat = 'Birthplace')]

remove_cols2 = g01.columns[g01.columns.str.contains(pat = 'Counted_Census_Night')]
remove_cols3 = g01.columns[g01.columns.str.contains(pat = 'Indig')]
remove_cols4 = g01.columns[g01.columns.str.contains(pat = 'Count_Census')]


# In[76]:


remove_cols4


# In[77]:


g01.drop(remove_cols1, axis=1, inplace = True)
g01.drop(remove_cols2, axis=1, inplace = True)
g01.drop(remove_cols3, axis=1, inplace = True)
g01.drop(remove_cols4, axis=1, inplace = True)


# In[78]:


g01.head()


# In[79]:


education_young_males = ['Age_psns_att_educ_inst_0_4_M','Age_psns_att_educ_inst_5_14_M','Age_psns_att_edu_inst_15_19_M']
education_young_females = ['Age_psns_att_educ_inst_0_4_F','Age_psns_att_educ_inst_5_14_F','Age_psns_att_edu_inst_15_19_F']
education_young_population = ['Age_psns_att_educ_inst_0_4_P','Age_psns_att_educ_inst_5_14_P','Age_psns_att_edu_inst_15_19_P']

education_middle_old_aged_male = ['Age_psns_att_edu_inst_20_24_M','Age_psns_att_edu_inst_25_ov_M']
education_middle_old_aged_female = ['Age_psns_att_edu_inst_20_24_F','Age_psns_att_edu_inst_25_ov_F']
education_middle_old_aged_population = ['Age_psns_att_edu_inst_20_24_P','Age_psns_att_edu_inst_25_ov_P']


# In[80]:


g01['education_young_males'] = g01[education_young_males].sum(axis=1)
g01['education_young_females'] = g01[education_young_females].sum(axis=1)
g01['education_young_population'] = g01[education_young_population].sum(axis=1)
g01['education_middle_old_aged_male'] = g01[education_middle_old_aged_male].sum(axis=1)
g01['education_middle_old_aged_female'] = g01[education_middle_old_aged_female].sum(axis=1)
g01['education_middle_old_aged_population'] = g01[education_middle_old_aged_population].sum(axis=1)


# In[81]:


g01.drop(education_young_males, axis = 1, inplace= True)
g01.drop(education_young_females, axis = 1, inplace= True)
g01.drop(education_young_population, axis = 1, inplace= True)
g01.drop(education_middle_old_aged_male, axis = 1, inplace= True)
g01.drop(education_middle_old_aged_female, axis = 1, inplace= True)
g01.drop(education_middle_old_aged_population, axis = 1, inplace= True)


# In[82]:


g01.head()


# In[83]:


higest_education_male_9_or_greater = ['High_yr_schl_comp_Yr_12_eq_M','High_yr_schl_comp_Yr_11_eq_M','High_yr_schl_comp_Yr_10_eq_M','High_yr_schl_comp_Yr_9_eq_M']
higest_education_female_9_or_greater = ['High_yr_schl_comp_Yr_12_eq_F','High_yr_schl_comp_Yr_11_eq_F','High_yr_schl_comp_Yr_10_eq_F','High_yr_schl_comp_Yr_9_eq_F']
higest_education_population_9_or_greater = ['High_yr_schl_comp_Yr_12_eq_P','High_yr_schl_comp_Yr_11_eq_P','High_yr_schl_comp_Yr_10_eq_P','High_yr_schl_comp_Yr_9_eq_P']


# In[84]:


g01['higest_education_male_9_or_greater'] = g01[higest_education_male_9_or_greater].sum(axis=1)
g01['higest_education_female_9_or_greater'] = g01[higest_education_female_9_or_greater].sum(axis=1)
g01['higest_education_population_9_or_greater'] = g01[higest_education_population_9_or_greater].sum(axis=1)

g01.drop(higest_education_male_9_or_greater, axis = 1, inplace= True)
g01.drop(higest_education_female_9_or_greater, axis = 1, inplace= True)
g01.drop(higest_education_population_9_or_greater, axis = 1, inplace= True)


# In[85]:


higest_education_male_9_or_greater


# In[86]:


#g01.drop(higest_education_female_9_or_greater, axis = 1, inplace= True)
#g01.drop(higest_education_population_9_or_greater, axis = 1, inplace= True)


# In[87]:


g01.head()


# In[91]:


g01.rename(columns={'higest_education_female_9_or_greater': 'higest_education_9_or_greater_female', 'higest_education_population_9_or_greater': 'higest_education_9_or_greater_population', 'higest_education_male_9_or_greater' : 'higest_education_9_or_greater_male'}, inplace = True)


# In[92]:


g01.head(1)


# In[93]:


g01.rename(columns = {'Tot_P_M': 'Total_population_Male', 'Tot_P_F': 'Total_population_Female', 'Tot_P_P':'Total_population'}, inplace=True)


# In[94]:


g01.head()


# In[95]:


g01.to_csv('g01_processed.csv')


# In[96]:


g02 = g01


# In[97]:


g02.drop('education_young_males',axis=1, inplace = True)
g02.drop('education_young_females',axis=1, inplace = True)
g02.drop('education_young_population',axis=1, inplace = True)
g02.drop('education_middle_old_aged_male',axis=1, inplace = True)
g02.drop('education_middle_old_aged_female',axis=1, inplace = True)
g02.drop('education_middle_old_aged_population',axis=1, inplace = True)


# In[104]:


g02.to_csv('g01_processed_with_removed_currently_att_ed_inst_cols.csv')


# In[101]:


g01.rename(columns = {'education_young_males':'currently_att_edu_inst_young_males','education_young_females':'currently_att_edu_inst_young_females'}, inplace=True)


# In[102]:


g01.rename(columns= {'education_young_population':'currently_att_edu_inst_young_population','education_middle_old_aged_male':'currently_att_edu_inst_middle_old_aged_male'}, inplace=True)
g01.rename(columns = {'education_middle_old_aged_female':'currently_att_edu_inst_middle_old_aged_female'}, inplace=True)
g01.rename(columns = {'education_middle_old_aged_population':'currently_att_edu_inst_middle_old_aged_population'}, inplace=True)


# In[105]:


g01.to_csv("g01_processed_v1.csv")


# In[ ]:




