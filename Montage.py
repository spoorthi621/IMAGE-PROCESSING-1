#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
from PIL import Image
from skimage import io


IMAGE_WIDTH = 400
IMAGE_HEIGHT = 400

def create_collage(images):
    images = [io.imread(img) for img in images]
    images = [cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT)) for image in images]
    if len(images) > 2:
        half = len(images) // 2
        h1 = cv2.hconcat(images[:half])
        h2 = cv2.hconcat(images[half:])
        concat_images = cv2.vconcat([h1, h2])
    else:
        concat_images = cv2.hconcat(images)
    image = Image.fromarray(concat_images)

    # Image path
    image_name = "montage.png"
    image = image.convert("RGB")
    image.save(f"{image_name}")
    return image_name
images=["im2.png","im4.png","im8.png","im10.png"]
#image1 on top left, image2 on top right, image3 on bottom left,image4 on bottom right
create_collage(images)


# In[5]:



import cv2
import numpy as np

# read all the images
# we are going to take 4 images only
image1=cv2.imread("im1.png")
image2=cv2.imread("im3.png")
image3=cv2.imread("im5.png")
image4=cv2.imread("im7.png")

# make all the images of same size
#so we will use resize function
image1=cv2.resize(image1,(200,200))
image2=cv2.resize(image2,(200,200))
image3=cv2.resize(image3,(200,200))
image4=cv2.resize(image4,(200,200))

# Now how we will attach image with other image
# we will create a horizontal stack of images
# then we will add it to the vertical stack
# let the horizontal pair be (image1,image2)
# and (image3,image4)
# we will use numpy stack function
Horizontal1=np.hstack([image1,image2])
Horizontal2=np.hstack([image3,image4])

# Now the horizontal attachment is done
# noe vertical attachment
Vertical_attachment=np.vstack([Horizontal1,Horizontal2])

# Show the final attachment
cv2.imshow("Final Collage",Vertical_attachment)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




