#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Remove BG

from PIL import Image,ImageDraw
img2 = Image.open("im7.png").convert("RGBA")
seed=(0,0)
rep_value=(0,0,0,0)
ImageDraw.floodfill(img2,seed,rep_value,thresh=100)

# Opening the primary image (used in background)
img1 = Image.open("gontu.jpg")


# Opening the secondary image (overlay image)

# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2, mask = img2)

# Displaying the image
img1.show()


# In[2]:


import cv2
from PIL import Image,ImageDraw,ImageFilter
img1 = Image.open("im1.png")
img2 = Image.open("im9.png")
mask=Image.new("L",img2.size,0)
draw=ImageDraw.Draw(mask)
draw.ellipse((50,10,300,350),fill=200)
mask_im_blur=mask.filter(ImageFilter.GaussianBlur(10))
back_im = img1.copy()
back_im.paste(img2,(0,0),mask_im_blur)
back_im.show()
cv2.waitKey(0)  
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




