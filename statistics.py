#!/usr/bin/env python
# coding: utf-8

# In[1]:


#converting image
from PIL import Image 
image = Image.open('im6.png')
image.save("img6.jpg")
print("Image successfully converted")


# In[2]:


#print mode
print(image.mode)


# In[ ]:


#Cropping
import cv2
im=cv2.imread('im7.png')
crop=im[50:200,100:400]
cv2.imshow("Original Image",im)
cv2.imshow("Cropped Image",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#writing on image
from PIL import Image,ImageDraw,ImageFont

im=Image.open('im1.png')
d1=ImageDraw.Draw(im)
font=ImageFont.truetype("calibri.ttf",100)
d1.text((100,200),"Hello,flower",fill=(250,0,0),font=font)
im.show()


# In[ ]:


#Image blending

im1=Image.open("gontu.jpg")
im2=Image.open("mintu.jpg")

alpha1=Image.blend(im1,im2,alpha=.4)
alpha2=Image.blend(im1,im2,alpha=.2)

alpha1.show()
alpha2.show()


# In[ ]:


#RGB Channels
import matplotlib.pyplot as plt
ch_r,ch_g,ch_b=im1.split()
plt.figure(figsize=(18,6))
plt.subplot(1,3,1);
plt.imshow(ch_r,cmap=plt.cm.Reds);plt.axis("off")
plt.subplot(1,3,2);
plt.imshow(ch_g,cmap=plt.cm.Greens);plt.axis("off")
plt.subplot(1,3,3);
plt.imshow(ch_b,cmap=plt.cm.Blues);plt.axis("off")
plt.tight_layout()
plt.show()


# In[ ]:


#negating image
im=Image.open("im6.png")
im_t=im.point(lambda x:255 -x)
im_t.show()


# In[ ]:


#histogram
im=Image.open("im6.png")
pl=im.histogram()
plt.bar(range(256),pl[:256],color='r',alpha=0.5)
plt.bar(range(256),pl[:256:2*256],color='g',alpha=0.4)
plt.bar(range(256),pl[2*256:],color='b',alpha=0.3)


# In[ ]:


#stat
#Mean
from PIL import Image,ImageStat
im=Image.open("im1.png")
stat=ImageStat.Stat(im)
print(stat.mean)


# In[ ]:


#Median
from PIL import Image,ImageStat
im=Image.open("im1.png")
stat=ImageStat.Stat(im)
print(stat.median)


# In[ ]:


#Standard Deviation
from PIL import Image,ImageStat
im=Image.open("im1.png")
stat=ImageStat.Stat(im)
print(stat.stddev)


# In[ ]:


#Drawing on an image
from PIL import Image,ImageDraw
im=Image.open("im2.png")
draw=ImageDraw.Draw(im)
draw.rectangle(xy=(50,50,150,150),fill=(0,127,0))
im.show()


# In[ ]:


#slicing
from skimage.io import imshow,imread
import matplotlib.pyplot as plt
im=imread("im1.png")
imshow(im)
fig,ax=plt.subplots(1,3,figsize=(6,4),sharey=True)

ax[0].imshow(im[:,0:130])
ax[0].set_title('First Split')

ax[1].imshow(im[:,130:260])
ax[1].set_title('Second Split')

ax[2].imshow(im[:,260:390])
ax[2].set_title('Third Split')


# In[ ]:





# In[ ]:




