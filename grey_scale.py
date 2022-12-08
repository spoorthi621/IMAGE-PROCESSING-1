#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
image = cv2.imread("im1.png",0)
cv2.imshow('images',image)


# In[2]:


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




