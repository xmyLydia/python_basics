#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.listdir()


# In[2]:


import pandas


# In[5]:


df1 = pandas.read_csv("supermarkets.csv")
df1


# In[7]:


df2 = pandas.read_json("supermarkets.json")
df2


# In[11]:


df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
df3


# In[13]:


df4 = pandas.read_csv("supermarkets-commas.txt")
df4


# In[18]:


df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep = ";")
df5


# In[20]:


from geopy.geocoders import ArcGIS


# In[21]:


nom = ArcGIS()


# In[24]:


n = nom.geocode("3995 23 rd, St, San Francisco, CA 94114")


# In[29]:


import pandas
df = pandas.read_csv("supermarkets.csv")
df


# In[30]:


df["Address"] = df["Address"] + ", " + df["City"]+ ", " + df["State"]+ ", " + df["Country"]
df


# In[34]:


df["Coordinate"] = df["Address"].apply(nom.geocode)
df


# In[37]:


df["Latitude"] = df["Coordinate"].apply(lambda x: x.latitude if x != None else None)

df["Longitude"] = df["Coordinate"].apply(lambda x: x.longitude if x != None else None)
df

