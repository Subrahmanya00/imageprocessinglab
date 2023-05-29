#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install opencv-python')
import cv2

print(cv2.__version__)


# In[ ]:


conda install -c conda-forge opencv


# In[6]:


get_ipython().system('pip install numpy scipy matplotlib scikit-learn jupyter')


# In[4]:


import matplotlib.pyplot as plt
import matplotlib.image as img

images=img.imread("C:/Users/CCL/Downloads/s.png")

plt.imshow(images)


# In[5]:


# code for displaying multiple images in one figure

#import libraries
import cv2
from matplotlib import pyplot as plt

# create figure
fig = plt.figure(figsize=(10, 7))

# setting values to rows and column variables
rows = 2
columns = 2

# reading images
Image1 = cv2.imread('C:/Users/CCL/Downloads/p.png')
Image2 = cv2.imread('C:/Users/CCL/Downloads/p.png')
Image3 = cv2.imread('C:/Users/CCL/Downloads/pause.png')
Image4 = cv2.imread('C:/Users/CCL/Downloads/play.png')

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(Image1)
plt.axis("on")
plt.title("First")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(Image2)
plt.axis('on')
plt.title("Second")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(Image3)
plt.axis('on')
plt.title("Third")

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)

# showing image
plt.imshow(Image4)
plt.axis('on')
plt.title("Fourth")


# In[6]:


import cv2 
import os 
import glob 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
 
mages = [plt.imread(file) for file in glob.glob("path/to/files/*.png")]
data = [] 
for f1 in files: 
    img = plt.imread(f1) 
    data.append(img) 
    plt.figure() 
    plt.imshow(img) 


# In[ ]:





# In[ ]:




