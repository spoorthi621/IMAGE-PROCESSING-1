#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Shading
import cv2

img = cv2.imread('shading.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', grayImg)
cv2.waitKey(0)
filtersize = 513
gaussianImg = cv2.GaussianBlur(grayImg, (filtersize, filtersize), 128)
cv2.imshow('Converted Image', gaussianImg)
cv2.waitKey(0)
newImg = (grayImg-gaussianImg)
cv2.imshow('New Image', newImg)
cv2.imwrite('Converted.png', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


# Box Filter
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('im9.png')
blur = cv2.blur(img,(100,100))

plt.imshow(img),plt.title('Original')
plt.show()
plt.xticks([]), plt.yticks([])
plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# In[21]:


#Countours using opencv
import cv2 
import numpy as np 

image = cv2.imread('im9.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0) 
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
cv2.imshow('Canny Edges After Contouring', edged)  
cv2.waitKey(0) 

print("Number of Contours: " + str(len(contours)))  
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)   
cv2.imshow('Contours', image)
cv2.waitKey(0) 

image2 = cv2.imread('im9.png')
if len(contours) != 0:
	c = max(contours, key = cv2.contourArea)
cv2.drawContours(image2, c, -1, (0, 255, 0), 3)
cv2.imshow('Largest Contour', image2)
cv2.waitKey(0) 

cv2.destroyAllWindows() 


# In[11]:


#Grab Cut
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('im6.png')
cv2.imshow('img', img)

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,52,450,500)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img_cut = img*mask2[:,:,np.newaxis]

cv2.imshow('img_cut', img_cut)
cv2.waitKey(0)


# In[ ]:





# In[ ]:




