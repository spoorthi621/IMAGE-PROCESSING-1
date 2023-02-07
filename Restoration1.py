#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Restore damaged Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
# Open the image.
img = cv2.imread('cat_damaged.png')
plt.imshow(img)
plt.show()
 
# Load the mask.
mask = cv2.imread('cat_mask.png', 0)
plt.imshow(mask)
plt.show()
 
# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
 
# Write the output.

cv2.imwrite('cat_inpainted.png',dst)
plt.imshow(dst)
plt.show()


# In[2]:


#Removing logos
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['figure.figsize']=(10,8)


# In[8]:


def show_image(image,title='Image',cmap_type='gray'):
    plt.imshow(image,cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
   
def plot_comparison(img_original,img_filtered,img_title_filtered):
    fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(10,8),sharex=True,sharey=True)
    ax1.imshow(img_original,cmap=plt.cm.gray)
    ax1.set_title('Original')
    #ax1.axis('off')
    ax2.imshow(img_filtered,cmap=plt.cm.gray)
    ax2.set_title(img_title_filtered)
    #ax2.axis('off')


# In[9]:


from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color


# In[14]:


image_with_logo = plt.imread('logo6.png')

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:-1])

# Set the pixels where the logo is to 1
mask[210:290, 360:425] = 1

# Apply inpainting to remove the logo
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo,
                                                mask,
                                                multichannel=True)

# Show the original and logo removed images
plot_comparison(image_with_logo, image_logo_removed, 'Image with logo removed') 


# In[ ]:




