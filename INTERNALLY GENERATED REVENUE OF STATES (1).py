#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np 


# In[ ]:





# In[2]:


Igr = pd.read_csv(r"C:\Users\User\Desktop\AI AND DATA SCIENCE BOOTCAMP\DATA SCIENCE\Jumia_clean Project work.csv")


# In[3]:


Igr.info()


# In[4]:


Igr.head(5)


# In[5]:


# Igr['brand'].replace(Phones_int, Phones, inplace = True)

Igr.rename(columns={'brand': 'Phone', 'ratings': 'clientrating'}, inplace=True)


# In[6]:


Igr.head(3)


# In[7]:


Igr.value_counts()


# In[8]:


Igr.keys()


# In[9]:


Igr.dropna()


# In[10]:


Igr.clientrating.mean()


# In[11]:


Igr.clientrating.median()


# In[12]:


Igr.clientrating.mode()


# In[13]:


Igr.head(3)


# In[20]:


Abstpf = Igr[Igr["clientrating"] == 3.5]


# In[21]:


Abstpf.mean()


# In[ ]:




