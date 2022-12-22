#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Median Filtering
import cv2
import numpy as np

#read image
img_noisy1=cv2.imread("gontu.jpg",0)

#obtain no of rows and columns
m,n=img_noisy1.shape

#traverse the image
img_new1=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[img_noisy1[i-1,j],
              img_noisy1[i-1,j+1],
              img_noisy1[i,j-1],
              img_noisy1[i,j],
              img_noisy1[i,j+1],
              img_noisy1[i+1,j-1],
              img_noisy1[i+1,j],
              img_noisy1[i-1,j-1],
              img_noisy1[i+1,j+1]]
       
        temp=sorted(temp)
        img_new1[i,j]=temp[4]
        img_new1=img_new1.astype(np.uint8)
       
cv2.imshow("Median filtered image",img_new1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


#Blurred
import cv2
import numpy as np
img=cv2.imread("gontu.jpg",0)
m,n=img.shape
mask=np.ones([3,3],dtype=int)
mask=mask/9
new=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=img[i-1,j-1]*mask[0,0]+img[i-1,j]*mask[0,1]+img[i-1,j+1]*mask[0,2]+img[i,j-1]*mask[1,0]+img[i,j]*mask[1,1]+img[i,j+1]*mask[1,2]+img[i+1,j-1]*mask[2,0]+img[i+1,j]*mask[2,1]+img[i+1,j+1]*mask[2,2]
        new[i,j]=temp
        new=new.astype(np.uint8)
cv2.imshow("blurred",new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:





# In[ ]:





# In[ ]:




