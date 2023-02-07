#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Image Sharpness
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
#Load the image
my_image=Image.open('abd.png')
#Use sharpen function
sharp=my_image.filter(ImageFilter.SHARPEN)
#Save the image
sharp.save('C:/Users/User/Downloads/Im/IS.png')
sharp.show()
plt.imshow(sharp)
plt.show()


# In[7]:


#Image flip
import matplotlib.pyplot as plt
#Load the image
img=Image.open('abd.png')
plt.imshow(sharp)
plt.show()
#use the flip function
flip=img.transpose(Image.FLIP_LEFT_RIGHT)

#save the image
flip.save('C:/Users/User/Downloads/Im/ImageFlip.png')
plt.imshow(flip)
plt.show()


# In[21]:


#Importing Image class from PIL module
from PIL import Image
import matplotlib.pyplot as plt
#opens image in RGB mode
im=Image.open('abd.png')

#size of img in pixels(size of original image)
#this is not mandatory
width,height=im.size

#cropped img of above dimension
#It will not change original image
im1=im.crop((50,50,1500,1500))

#shows image in image viewer
im1.show()
plt.imshow(im1)
plt.show()


# In[ ]:




