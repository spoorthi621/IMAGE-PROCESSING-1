#!/usr/bin/env python
# coding: utf-8

# In[1]:



import cv2
import numpy as np

img = cv2.imread('snow.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', img)

blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('blur', blur)

ret,th1 = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
cv2.imshow('Global', th1)
cv2.imwrite('Global.jpg',th1)


th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Mean', th2)
cv2.imwrite('AM.jpg',th2)


th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Gaussian', th3)
cv2.imwrite('AG.jpg',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:


import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


# In[ ]:




