#!/usr/bin/env python
# coding: utf-8

# In[25]:


# import OS module
import os
 
# Get the list of all files and directories
path = "C:/Users/CCL/Downloads"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files


for dir_list in os.listdir(path):
 
    # check if the image ends with png
    
        print(dir_list)


# In[2]:


import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/CCL/Downloads"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)


# In[3]:


import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/CCL/Downloads"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".jpg")):
        print(images)


# In[14]:


import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/CCL/Downloads"
for media in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (media.endswith(".exe")):
        print(media)


# In[ ]:




