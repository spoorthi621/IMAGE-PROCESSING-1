#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Down-Sampling
import cv2

image = cv2.imread('im1.png')
print("Size of image before pyrDown: ", image.shape)

image = cv2.pyrDown(image)
print("Size of image after pyrDown: ", image.shape)
cv2.imshow('DownSample', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#Up-Sampling
import cv2
image = cv2.imread('im8.png')
print("Size of image before pyrDown: ", image.shape)

image = cv2.pyrUp(image)
print("Size of image after pyrUp: ", image.shape)
cv2.imshow('DownSample', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


#Quantization

# Importing Image module from PIL package
from PIL import Image
import PIL

# creating a image object (main image)
im1 = Image.open("im4.png")

# quantize a image
im1 = im1.quantize(6)

# to show specified image
im1.show()


# In[11]:


#Down-Sampling
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('im1.png')
print("Size of image before pyrDown: ", image.shape)

image = cv2.pyrDown(image)
print("Size of image after pyrDown: ", image.shape)
cv2.imshow('DownSample', image)
plt.imshow(image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




