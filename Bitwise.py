#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
img1 = cv.imread("mintu.jpg")
img2 = cv.imread("gontu.jpg")
cv.imshow('img1',img1)
cv.imshow('img2',img2)

cv.waitKey(0)  
cv.destroyAllWindows()


# In[2]:


#AND
bitwise_AND = cv.bitwise_and(img1, img2)
cv.imshow('AND',bitwise_AND)

cv.waitKey(0)  
cv.destroyAllWindows()


# In[3]:


#OR
bitwise_OR = cv.bitwise_or(img1, img2)
cv.imshow('OR',bitwise_OR)

cv.waitKey(0)  
cv.destroyAllWindows()


# In[4]:


#NOT
bitwise_NOT = cv.bitwise_not(img1)
cv.imshow('NOT',bitwise_NOT)

cv.waitKey(0)  
cv.destroyAllWindows()


# In[ ]:





# In[6]:





# In[29]:





# In[ ]:




