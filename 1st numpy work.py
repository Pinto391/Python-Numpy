#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


a= np.array([[5,6,7],[4,8,9]], dtype=float)
a.dtype


# In[6]:


a.ndim


# In[7]:


a.itemsize


# In[8]:


a


# In[9]:


a.size


# In[11]:


a.shape


# In[12]:


np.zeros((4,3))


# In[17]:


q=np.ones((4,3))


# In[18]:


np.arange(1,20,3)


# In[19]:


np.linspace(1,20,10)


# In[24]:


q.reshape(12,1)


# In[25]:


q.ravel()


# In[26]:


q


# In[29]:


p=np.array([[1,2],[3,4],[5,6]])


# In[30]:


p


# In[32]:


p.min()


# In[33]:


p.max()


# In[34]:


p.sum()


# In[35]:


p.sum(axis=0)


# In[36]:


p.sum(axis=1)


# In[38]:


np.std(p)


# In[41]:


x= np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
x


# In[42]:


y


# In[43]:


x+y


# In[44]:


x.dot(y)


# In[ ]:




