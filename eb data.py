#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pymongo as pm


# In[90]:


from pymongo import MongoClient
client = MongoClient()


# In[91]:


client = pymongo.MongoClient('localhost',27017)
db = client['eb']
print(db.list_collection_names())
mycol=db["users"]


# In[92]:


x = mycol.find_one()

print(x)


# In[93]:


display(x)


# In[94]:


db.users.count()


# In[95]:


cursor = mycol.find() 
for record in cursor: 
    print(record.keys())
    print(len(record.keys()))


# In[96]:


for record in cursor: 
    print(len(record.key()))


# In[97]:


a = mycol.find().count()
print(a)


# In[112]:


import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
plt.bar(list(record.keys(),record.values())
    plt.show()


# In[114]:


cursor = mycol.find() 
for record in cursor: 
    plt.bar(record.keys(),color='g')
    plt.show()


# In[115]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='green')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x_pos, x)

plt.show()


# In[136]:


for i in range (0,8969):
    print (i)


# In[152]:


a = []
for i in range (0,8968):
        a.append(str(i))
print(a)


# In[153]:


cursor = mycol.find()
b=[]
for record in cursor: 
    #print(record.keys())
    #print(len(record.keys()))
    b.append(len(record.keys()))
print(b)


# In[155]:


len1=len(a)
print(x)
len2=len(b)
print(y)


# In[157]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

x = a
y = b

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y, color='green')
plt.xlabel("count of users")
plt.ylabel("value of dictionary")
plt.title("graph")

plt.xticks(x_pos, x)

plt.show()


# In[ ]:




