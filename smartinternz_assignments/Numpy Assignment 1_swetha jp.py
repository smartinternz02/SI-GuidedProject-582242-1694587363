#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# # Import NumPy as np
# ## done by: jpswetha 
# ## reg no:21blc1407

# In[ ]:


import numpy as np


# #### Create an array of 10 zeros 

# In[ ]:


z=np.zeros(10)
z


# #### Create an array of 10 ones

# In[ ]:


x=np.ones(10)
x


# #### Create an array of 10 fives

# In[ ]:


np.ones(10) * 5


# #### Create an array of the integers from 10 to 50

# In[ ]:


np.arange(10,51,1)


# #### Create an array of all the even integers from 10 to 50

# In[ ]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[ ]:


np.arange(9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[ ]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[ ]:


np.ramdom.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[ ]:


np.random.randn(25)


# #### Create the following matrix:

# In[ ]:


np.arrange(0.01,1.01,step=0.01,dtype=float)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[ ]:


np.linspace(0, 1, 20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[ ]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:


a[2:, 1:]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[7]:


a[3,4]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:


a[:3, 1].reshape(-1, 1)


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:


a[4, :]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:


a[3:, :]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[ ]:


np.sum(a)


# #### Get the standard deviation of the values in mat

# In[ ]:


np.sd(a)


# #### Get the sum of all the columns in mat

# In[ ]:


np.sum(a,axis=0)


# 
