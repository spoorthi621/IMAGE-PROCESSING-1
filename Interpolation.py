#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Interpolation
import cv2
import numpy as np

img = cv2.imread('gontu.jpg')
near_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_NEAREST)
cv2.imshow('Near',near_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np
img = cv2.imread('gontu.jpg')
bilinear_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Bilinear',bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

img = cv2.imread('gontu.jpg')
bicubic_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Bicubic',bicubic_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




