#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


#from internal drive
image = cv2.imread("im1.png")
cv2.imshow('images',image)


# In[3]:


cv2.imwrite('D:/img.png',image)


# In[4]:


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#From extenal drive

image = cv2.imread("C:/Users/User/Downloads/Im/im6.png")
cv2.imshow('images',image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


#height and width of image
from PIL import Image

x="im2.png"
img=Image.open(x)

width=img.width
height=img.height

print("The Height Of The Image Is:",height)
print("The Width Of The Image Is:",width)


# In[7]:


#Number of channels of grey_scale image
import cv2
image = cv2.imread("im1.png",0)
print("no of channels is:" +str(image.ndim))
print("no of channels is:",image.shape)
cv2.imshow('images',image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


#Number of channels of image
image = cv2.imread("im1.png")
print("no of channels is:" +str(image.ndim))
print("no of channels is:",image.shape)
cv2.imshow('images',image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


#resize image
from PIL import Image
filepath="im4.png"
im=Image.open(filepath)
new_im=im.resize((500,500))
new_im


# In[10]:


#Matrix representatio of image

import matplotlib.image as image
img=image.imread("f.jpg")
print("The shape of the image is",img.shape)
print("The array of image is")
print(img)


# In[11]:


#load the binary image

import cv2

img=cv2.imread("im6.png",0)
ret,bw_img=cv2.threshold(img,127,300,cv2.THRESH_BINARY)
bw=cv2.threshold(img,300,127,cv2.THRESH_BINARY)
cv2.imshow("Binary",bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[19]:


#display The BGR channels

import cv2
img = cv2.imread("im1.png",1)
B,G,R = cv2.split(img)
print(B)
print(G)
print(R)


# In[20]:


img = cv2.imread("im1.png",1)
cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[21]:


cv2.imshow("Blue",B)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:


cv2.imshow("Red",B)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[23]:


cv2.imshow("Green",B)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[25]:


#aspect ratio

import cv2
img=cv2.imread("im6.png")
new_im=img.resize((400,200))
ar=1*(img.shape[1]/img.shape[0])
print("Aspect ratio")
print(ar)


# In[ ]:




