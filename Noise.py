#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Adding Noise
import matplotlib.pyplot as plt
from skimage.util import random_noise
fruit=plt.imread("fruit.jpg")

#Add noise to the image
noisy_image=random_noise(fruit)

#show the original
plt.title("Original")
plt.imshow(fruit)
plt.show()

#show noisy image
plt.title("Noisy Image")
plt.imshow(noisy_image)
plt.show()


# In[8]:


#reducing noisy
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle
noisy_image = plt.imread("noisy.jpg")
denoised_image = denoise_tv_chambolle(noisy_image, multichannel = True)
plt.title("original")
plt.imshow(noisy_image)
plt.show()
plt.title("noisy reduced image")
plt.imshow(denoised_image)
plt.show()


# In[9]:


#Reducing Noise while preserving edges
import matplotlib.pyplot as plt
from skimage.restoration import denoise_bilateral
landscape_img = plt.imread("noisy.jpg")
denoised_img = denoise_bilateral(landscape_img, multichannel = True)
plt.title("original")
plt.imshow(landscape_img)
plt.show()
plt.title("DEnoised")
plt.imshow(denoised_img)
plt.show()


# In[19]:


#segmentation
from skimage.segmentation import slic
from skimage.color import label2rgb
face_image = plt.imread("face.jpg")
segments = slic(face_image, n_segments = 400)
segmented_image = label2rgb(segments, face_image, kind = 'avg')
plt.title("original")
plt.imshow(face_image.astype('uint8'))
plt.show()
plt.title("segmented image")
plt.imshow(segmented_image.astype('uint8'))
plt.show()


# In[12]:


#Contouring shapes
def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:,1], contour[:, 0], linewidth= 3)
    plt.imshow(image, interpolation = 'nearest', cmap= 'gray_r')
    plt.title("contours")
    plt.axis("off")


# In[13]:


from skimage import measure, data
horse_image = data.horse()
contours = measure.find_contours(horse_image, level = 0.8)
show_image_contour(horse_image, contours)


# In[14]:


def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:,1], contour[:, 0], linewidth= 3)
    plt.imshow(image, interpolation = 'nearest', cmap= 'gray_r')
    plt.title("contours")
    plt.axis("off")
   
from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage import color

image_dices = imread("dice.png")

image_dices = color.rgb2gray(image_dices)

thresh = threshold_otsu(image_dices)

binary = image_dices > thresh

contours = measure.find_contours(binary, level = 0.8)

show_image_contour(image_dices, contours)


# In[15]:


def show_image_contour(image, contours):
    plt.figure()
    for n, contour in enumerate(contours):
        plt.plot(contour[:,1], contour[:, 0], linewidth= 3)
    plt.imshow(image, interpolation = 'nearest', cmap= 'gray_r')
    plt.title("contours")
    plt.axis("off")
import numpy as np
shape_contours  = [cnt.shape[0] for cnt in contours]
max_dots_shape = 50
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0]<max_dots_shape]
show_image_contour(binary, contours)
print("dice dots number:{}.".format(len(dots_contours)))


# In[ ]:




