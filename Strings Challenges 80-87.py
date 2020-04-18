#!/usr/bin/env python
# coding: utf-8

# In[2]:


first_name  = input("enter your first name: ")
f_len = len(first_name)
print("Length of First Name ", f_len)
last_name = input("Enter the last name: ")
l_len = len(last_name)
print("Length for last name is: ", l_len)

full_name = first_name + " " + last_name

full_len = len(full_name)

print("Your name is ", full_len, " characters long")


# In[4]:


sub = input("Enter your fvt subject: ")

for letter in sub:
    print(letter, end = "-")


# In[6]:


name = input("Enter your name in upper case: ")

while not name.isupper():
    print("not in upper, try again")
    name = input("Enter your name in upper case: ")

print("All in upper")
    


# In[11]:


car_num = input("Enter your car num plate number: ")

state = car_num[0:2]
rest_num = car_num[2:]

u_state = state.upper()

modified_number = u_state+rest_num

#print(state)
#print(rest_num)
print(modified_number)
    


# In[12]:


vowels = 'aeiou'
count = 0
name = input("enter the name: ")

for letter in name:
    if letter in vowels:
        count = count+1
        
print(count)
    


# In[13]:


#either create vowels as string or list. both will work
vowels = ['a','e','i','o','u']
count = 0
name = input("enter the name: ")

for letter in name:
    if letter in vowels:
        count = count+1
        
print(count)
    


# In[15]:


password = input("Please enter the password: ")
confirm = input("Please confirm the password: ")

if password == confirm:
    print("Thank you")
elif password.lower() == confirm.lower():
    print("Please enter in same case")
else:
    print("Incorrect")


# In[22]:


name = input("Please enter the name: ")

for i in range (len(name)-1,0-1, -1): #range gives the numeric and stop/2nd argument is not inclusive
    print(name[i])


length = len(name)
position =1
for i in name:
    new_position = length - position
    letter = name[new_position]
    print(letter)
    position = position+1
    
    


# In[ ]:




