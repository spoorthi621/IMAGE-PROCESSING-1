#!/usr/bin/env python
# coding: utf-8

# In[18]:


#find differnce between images
# import module
import matplotlib.pyplot as plt
from PIL import Image, ImageChops

# assign images
img1 = Image.open("diff1.jpg")
plt.imshow(img1)
plt.show()
img2 = Image.open("diff2.jpg")
plt.imshow(img2)
plt.show()

# finding difference
diff = ImageChops.difference(img1, img2)
plt.imshow(diff)
plt.show()


# In[ ]:




