#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Python program to illustrate
# arithmetic operation of
# bitwise AND of two images
	
# organizing imports
import cv2
import numpy as np
	
# path to input images are specified and
# images are loaded with imread command
img1 = cv2.imread('C:/Users/CCL/Downloads/po.jfif')
img2 = cv2.imread('C:/Users/CCL/Downloads/n.jfif')

# cv2.bitwise_and is applied over the
# image inputs with applied parameters
dest_not = cv2.bitwise_not(img2, img1, mask = None)

# the window showing output image
# with the Bitwise AND operation
# on the input images
cv2.imshow('Bitwise not', dest_not)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()


# In[10]:


# Python program to illustrate
# arithmetic operation of
# bitwise NOT on input image
	
# organizing imports
import cv2
import numpy as np
	
# path to input images are specified and
# images are loaded with imread command
img1 = cv2.imread('C:/Users/CCL/Downloads/po.jfif')
img2 = cv2.imread('C:/Users/CCL/Downloads/n.jfif')

# cv2.bitwise_not is applied over the
# image input with applied parameters
dest_not1 = cv2.bitwise_not(img1, mask = None)
dest_not2 = cv2.bitwise_not(img2, mask = None)

# the windows showing output image
# with the Bitwise NOT operation
# on the 1st and 2nd input image
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()


# In[ ]:




