#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Restore Image
import numpy as np
import cv2

# Open the image.
img = cv2.imread('cat_damaged.png')

# Load the mask.
mask = cv2.imread('cat_mask.png', 0)

# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

# Write the output.
cv2.imwrite('cat_inpainted.png', dst)

cv2.imshow("image",img)
cv2.imshow("mask",mask)
cv2.imshow("restored image",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




