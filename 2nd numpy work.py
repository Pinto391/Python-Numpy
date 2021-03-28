#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


n=np.array([1,2,3,4,5,6])


# In[4]:


n[2:5]


# In[5]:


n[-1]


# In[6]:


a=np.array([[6,7,8],[1,2,3],[9,3,2]])


# In[8]:


a[1,2]


# In[11]:


a[1:3,1]


# In[12]:


a[-1]


# In[14]:


a[-1,1:3]


# In[15]:


a[:,1:3]


# In[16]:


x= np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])


# In[17]:


np.vstack((x,y))


# In[18]:


np.hstack((x,y))


# In[22]:


q=np.arange(30).reshape(2,15)


# In[23]:


q


# In[26]:


result=np.hsplit(q,3)


# In[27]:


result[1]


# In[29]:


result=np.vsplit(q,2)


# In[30]:


result[1]


# In[32]:


z=np.arange(12).reshape(3,4)
z


# In[36]:


b=z>4
b


# In[37]:


z[b]


# In[38]:


z[b]=-5
z


# In[ ]:




